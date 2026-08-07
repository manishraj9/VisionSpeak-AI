
# 🎙️ VisionSpeak AI
### AI-Powered Image-to-Story & Text to Speech Generator using Google Gemini Vision
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

<p align="center">
  <img src="audio-img/app-snapshot.jpg" width="900">
</p>

## 🌟 Overview

VisionSpeak AI is an AI-powered multimodal application that transforms uploaded images into meaningful scene descriptions, creative stories, and natural-sounding speech.

Powered by **Google Gemini Vision** for image understanding and story generation, and **gTTS** for Text-to-Speech synthesis, the application provides an interactive experience through a modern Streamlit interface.

---

## 🚀 Live Demo

🌐 https://visionspeak-ai.streamlit.app/

---

## ✨ Features

- 🖼️ Upload JPG, JPEG, and PNG images
- 🤖 AI-powered image understanding using Google Gemini
- 📝 Generate detailed image descriptions
- 📖 Create creative stories from uploaded images
- 🔊 Convert stories into natural Text-to-Speech audio
- ▶️ Listen to generated audio directly
- 📥 Download generated stories
- 🎵 Download generated audio
- 🎨 Interactive Streamlit user interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini AI
- Google GenAI SDK
- gTTS
- Pillow
- python-dotenv

---

## 📂 Project Structure

```
VisionSpeak-AI
│── app.py
│── requirements.txt
│── README.md
│── utils/
│── img/
│── audio-img/
│── img-audio/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/manishraj9/VisionSpeak-AI.git
```

Move into the project

```bash
cd VisionSpeak-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

<img width="1919" height="875" alt="Screenshot 2026-08-08 004208" src="https://github.com/user-attachments/assets/ce2527af-fec3-4341-8e77-a9a0a6c589a5" />
<img width="1917" height="878" alt="Screenshot 2026-08-08 004235" src="https://github.com/user-attachments/assets/2de587d5-83a2-4078-a16a-623ad16dd5a9" />
<img width="1919" height="875" alt="Screenshot 2026-08-08 004308" src="https://github.com/user-attachments/assets/1355b854-d47a-4764-b737-13455e07d553" />

<img width="1910" height="873" alt="Screenshot 2026-08-08 005813" src="https://github.com/user-attachments/assets/19c6341c-5ccc-4326-bf30-050ea0d42463" />

<img width="1917" height="877" alt="Screenshot 2026-08-08 012216" src="https://github.com/user-attachments/assets/d2e4e73a-064b-4e73-8dec-3cc0e013757d" />

<img width="745" height="713" alt="Screenshot 2026-08-08 012248" src="https://github.com/user-attachments/assets/96346ba7-1214-4094-a581-3cfaaaa73f29" />









### Home Page

<img src="audio-img/app-snapshot.jpg" width="900">

---

## 🎯 Workflow

```
Image Upload
      │
      ▼
Google Gemini Vision
      │
      ▼
Scene Description
      │
      ▼
Creative Story Generation
      │
      ▼
gTTS Text-to-Speech
      │
      ▼
Audio Playback & Download
```

---
<img width="781" height="301" alt="system-design drawio" src="https://github.com/user-attachments/assets/0db66890-c938-4fac-86a3-d3e78a568194" />



## 📌 Future Improvements

- 🌍 Multi-language support
- 🎙️ Multiple AI voices
- 📄 PDF story export
- 🎨 Enhanced UI/UX
- 🎭 Story style selection (Fantasy, Horror, Sci-Fi, Kids)
- ☁️ Cloud storage integration

---

## 🤝 Contributing

Contributions are welcome!

Feel free to fork the repository, create a feature branch, and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Manish Raj Aryan**

- GitHub: https://github.com/manishraj9

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub!
