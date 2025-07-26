---
title: "Pixel - Multimodal AI Assistant"
emoji: "🤖"
colorFrom: "gray"
colorTo: "red"
sdk: "streamlit"
sdk_version: "1.47.0"
app_file: "streamlit_app.py"
pinned: true
---

# 🤖 Pixel - Your Multimodal AI Assistant

**Pixel** is a powerful, intelligent, and easy-to-use multimodal assistant that can **caption images**, **generate visuals from text**, and **chat conversationally** — all inside a sleek Streamlit app.

> Built for the **PAK Angels Cohort 6 Hackathon** by a passionate team, this assistant blends cutting-edge AI into one unified tool for creativity and productivity.

---

## ✨ Features

🔹 **Image Captioning**  
Upload an image, and Pixel will describe what it sees using advanced vision-language models.

🔹 **Text-to-Image Generation**  
Type a prompt and watch Pixel bring it to life as a high-quality image.

🔹 **Conversational Chat**  
Talk to Pixel naturally — ask questions, get help, or just have a chat, powered by Groq’s ultra-fast LLMs.

---

## 👨‍👩‍👧‍👦 Team

This project was proudly developed as part of the **PAK Angels Cohort 6 Hackathon** by:

- **Saad Toor**  
- **Anam Jafar**  
- **Dr. Rabia Javed**  
- **Kashif Khan**  
- **Hafiz Muhammad Adnan**  
- **Aneela Fatima**

---

## 🚀 Demo

Run it live on [Hugging Face Spaces](https://huggingface.co/spaces/saadtoorx/pixel-multimodal-ai-assistant)

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Streamlit 1.35.0**
- **Hugging Face Transformers & Diffusers**
- **Groq API (LLM backend)**
- **PIL (Pillow)**

---

## 🧠 How It Works

Each mode is powered by dedicated AI capabilities:

| Mode              | Backend / Model              | Description                               |
|------------------|------------------------------|-------------------------------------------|
| Image Captioning | Vision Transformer (e.g. BLIP) | Describes images in natural language      |
| Image Generation | Stable Diffusion             | Generates high-quality visuals from text  |
| Chat              | Groq API (Mixtral)           | Fast and helpful conversational agent     |

---

## 📸 Screenshots

| Captioning | Image Generation | Chat |
|------------|------------------|------|
| ![caption](images/sample_caption.png) | ![generation](images/sample_generation.png) | ![chat](images/sample_chat.png) |

---

## 📁 Project Structure

```
pixel-multimodal-ai-assistant/
│
├── app.py                     # Main Streamlit app
├── image_captioning.py        # Image-to-text functionality
├── image_generator.py         # Text-to-image functionality
├── groq_handler.py            # Chat via Groq API
├── .env                       # Secret keys (not committed)
├── requirements.txt           
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/saadtoorx/pixel-multimodal-ai-assistant.git
cd pixel-multimodal-ai-assistant
```

### 2. Create a `.env` file

Add your API key for Groq:

```
GROQ_API_KEY=your_groq_api_key_here
```

> ✅ Your `.env` file is **ignored by Git** and won’t be pushed to GitHub.

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Launch the App

```bash
streamlit run app.py
```

---

## 🧪 Example Prompts

- Image Captioning:  
  Upload an image of a dog sitting on grass.

- Image Generation:  
  `"a futuristic city with flying cars at sunset"`

- Chat:  
  `"Explain how transformers work in AI."`

---

## 🌐 Live Space

Check it out live on Hugging Face 👉 [https://huggingface.co/spaces/saadtoorx/pixel-multimodal-ai-assistant](https://huggingface.co/spaces/saadtoorx/pixel-multimodal-ai-assistant)

---

## 🪪 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

Huge thanks to:

- **PAK Angels Team & Mentors**  
- **Hugging Face & Streamlit Communities**  
- **Groq** for providing lightning-fast language model access

---

## 🤝 Contributions

Feel free to fork, star, and suggest improvements via PR or issue. Collaboration is welcome!

---
