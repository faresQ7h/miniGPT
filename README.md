# Local AI Chatbot (miniGPT)

A simple local AI chatbot built using LLaMA3 via Ollama.  
The project runs completely on your machine without any API key.

---

## Features

- Runs locally (no internet needed after first setup)
- No API key required
- Conversation memory (chat history)
- Automatic setup using Python (installs dependencies if missing)
- Cross-platform support (Linux, macOS, Windows*)

\* Windows requires manual Ollama installation

---

## How it works

This project uses:
- **Ollama** to run a local large language model (LLaMA3)
- A Python script to send and receive messages through a local API
- A setup script (`run.py`) that prepares everything automatically

---

## Requirements

- Python 3 installed
- Internet connection (only for first run to download the model)

---

## Installation & Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/local-ai-chatbot.git
cd local-ai-chatbot