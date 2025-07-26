import streamlit as st
from PIL import Image

from image_captioning import generate_caption
from image_generator import generate_image
from groq_handler import ask_groq

# --- UI Configuration ---
# Set the page title and layout for a wider, more centered application view.
st.set_page_config(page_title="Pixel - Your Multimodal AI Assistant", layout="centered")

# Initialize busy state in Streamlit's session_state.
# This prevents users from triggering multiple actions simultaneously.
if "busy" not in st.session_state:
    st.session_state["busy"] = False

# Display the main title of the application using Markdown for custom styling.
st.markdown("""
    <h1 style='text-align: center; font-size: 3em;'>PIXEL</h1>
    <h3 style='text-align: center; font-size: 1.5em; color: #666;'>Your Multimodal AI Assistant</h3>
""", unsafe_allow_html=True)

# --- Mode Toggler ---
# Radio buttons to switch between different AI modes.
# If a task is in progress, disable mode switching and inform the user.
if not st.session_state["busy"]:
    mode = st.radio(
        "Choose a mode:",
        ("Image Captioning", "Image Generation", "Chat"),
        horizontal=True, # Display options horizontally for a cleaner look.
        key="mode_selector" # Add a key for consistent behavior.
    )
else:
    st.info("A task is in progress. Please wait for it to finish before switching modes.")
    # Keep the currently active mode selected if busy.
    mode = st.session_state.get("active_mode", "Image Captioning")

# Store the active mode in session state to persist it during busy times.
st.session_state["active_mode"] = mode

# --- Centralized Content based on Mode ---

# --- Image Captioning Mode ---
if mode == "Image Captioning":
    st.header("🖼️ Image Captioning")
    st.markdown("Upload an image, and I'll tell you what I see.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image clearly.
        image = Image.open(uploaded_file)
        st.image(image, caption="Your Uploaded Image", use_container_width=True)

        # Button to trigger caption generation. Disabled when busy.
        if st.button("Generate Caption", disabled=st.session_state["busy"], key="generate_caption_btn"):
            st.session_state["busy"] = True # Set busy state.
            with st.spinner("Pixel is thinking..."): # Show a spinner while processing.
                image_bytes = uploaded_file.getvalue()
                caption = generate_caption(image_bytes)
                st.success("Here's the caption:") # Indicate success.
                st.write(caption) # Display the generated caption.
            st.session_state["busy"] = False # Reset busy state.

# --- Image Generation Mode ---
elif mode == "Image Generation":
    st.header("✨ Image Generation")
    st.markdown("Give me a prompt, and I'll create an image for you.")

    prompt = st.text_input("Enter a prompt for the image:", key="image_prompt_input")

    # Button to trigger image generation. Disabled when busy.
    if st.button("Generate Image", disabled=st.session_state["busy"], key="generate_image_btn"):
        if prompt:
            st.session_state["busy"] = True # Set busy state.
            with st.spinner("Pixel is creating... this might take a moment!"): # Show a spinner.
                generated_image = generate_image(prompt)
                if generated_image:
                    st.image(generated_image, caption=f"Generated Image for: '{prompt}'", use_container_width=True)
                else:
                    st.error("Sorry, I couldn't create the image. Please try again.")
            st.session_state["busy"] = False # Reset busy state.
        else:
            st.warning("Please enter a prompt to generate an image.")


# --- Chat Mode ---
elif mode == "Chat":
    st.header("💬 Chat with Pixel")
    st.markdown("Ask me anything! Your conversation with Pixel will appear below.")

    # Initialize chat history if it doesn't exist.
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat messages in a more conversational layout.
    # Iterating through history to show user and bot messages.
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            # Use st.chat_message for a distinct user message bubble.
            with st.chat_message("user"):
                st.write(msg["content"])
        else:
            # Use st.chat_message for a distinct bot message bubble.
            with st.chat_message("assistant"): # 'assistant' role often used for bots.
                st.write(msg["content"])

    # Input area for new messages, placed at the bottom for a natural chat flow.
    # st.chat_input is ideal for this, acting like a message bar.
    user_input = st.chat_input("Type your message here...", disabled=st.session_state["busy"])

    # If user types a message, process it.
    if user_input: # st.chat_input returns the message directly, no need for a separate button click.
        st.session_state["busy"] = True # Set busy state.

        # Add user message to history and immediately display it.
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input) # Display the just-sent user message.

        # Show a spinner while waiting for Pixel's response.
        with st.spinner("Pixel is typing..."):
            # Get Groq response.
            response = ask_groq(user_input)
            # Add bot's response to history and display it.
            st.session_state.chat_history.append({"role": "bot", "content": response})
            with st.chat_message("assistant"):
                st.write(response)

        st.session_state["busy"] = False # Reset busy state.

    # Optional: Clear chat history button.
    # Place it at the bottom for easy access without cluttering the main UI.
    if st.session_state.chat_history and not st.session_state["busy"]:
        if st.button("Clear Chat History", key="clear_chat_btn"):
            st.session_state.chat_history = [] # Clear the list.
            st.rerun() # Rerun the app to refresh the display.