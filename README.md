# Local AI Chatbot (miniGPT)

This is a simple local AI chatbot I built using LLaMA3 through Ollama.  
It runs completely on my machine without using any external API or paid service.

---

## What this project does

- Runs a chatbot locally (no API key needed)
- Keeps basic conversation memory
- Automatically sets up the environment (Python + Ollama + model)
- Works on Linux and macOS (Windows requires manual Ollama install)

---

## How it works

The project uses:
- **Ollama** to run a local large language model (LLaMA3)
- A Python script to send requests to the model through a local API
- A setup script (`run.py`) that installs and prepares everything automatically

---

## How to run

Make sure you have **Python 3 installed**:

```bash
python3 --version
