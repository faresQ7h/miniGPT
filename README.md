# 🧠 miniGPT – Local AI Chatbot

miniGPT is a simple AI chatbot that runs entirely on your local machine using the **LLaMA3** model via **Ollama**.

No API keys. No cloud. Everything stays on your device.

---

## ✨ Features

- **Fully local** – runs offline after setup
- **LLaMA3 model** – real LLM, not a fake chatbot
- **Ollama integration** – easy model management
- **Session memory** – remembers conversation during runtime
- **Automated setup** – one command to install and run everything

---

## 🧠 How It Works

The project consists of two main scripts:

### 1. miniGPT.py

- Sends user input to:
  http://localhost:11434/api/chat
- Stores messages in a list (conversation memory)
- Prints formatted AI responses in terminal

### 2. run.py

Handles everything automatically:

- Installs missing Python packages (requests)
- Checks if Ollama is installed
- Installs Ollama if needed (Linux/macOS)
- Starts Ollama server
- Downloads llama3 model
- Runs the chatbot

---

### ✅ Prerequisites

Check Python:
```
python3 --version
```
If not installed (Ubuntu/Debian):
```
sudo apt update
sudo apt install python3 python3-pip -y
```
---

## 📥 Installation

git clone https://github.com/faresQ7h/miniGPT.git
cd miniGPT

---

## ▶️ How to Run
```
python3 run.py
```
This will:

- install dependencies
- install/start Ollama
- download LLaMA3
- launch the chatbot

---

## 💬 Usage

Example:
```
You > Hello  
AI > Hi! How can I help you?
---
```
### ❌ Exit
```exit```

---

## ⚠️ Notes

- First run may take time (model download)
- If Ollama fails to install automatically:
  https://ollama.com/download
- Works best on Linux/macOS
- Windows may need manual Ollama setup

---

## 📌 Summary

miniGPT is a lightweight local chatbot that:

- runs fully offline
- uses LLaMA3
- requires no API keys
- keeps your data private

---

## 👤 Author

Fares
