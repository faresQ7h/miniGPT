# Local AI Chatbot (miniGPT)

This project is a simple local AI chatbot built using LLaMA3 through Ollama.  
It runs completely on your machine, so no API key or external service is required.

---

## What this project does

- Runs a chatbot locally on your computer
- Uses a real LLM (LLaMA3) through Ollama
- Keeps basic conversation memory during the session
- Automatically installs and prepares everything using `run.py`

---

## How it works

The system is made of two parts:

1. **Ollama**  
   Runs the AI model locally and exposes a local API (`http://localhost:11434`)

2. **Python chatbot (miniGPT.py)**  
   Sends your messages to the model and prints responses

3. **Setup script (run.py)**  
   Handles everything automatically:
   - installs missing dependencies
   - installs Ollama (if needed)
   - downloads the model
   - starts the AI server
   - launches the chatbot

---

## Requirements

You must have **Python 3 installed**.

### Check if Python is installed:

```bash
python3 --version
