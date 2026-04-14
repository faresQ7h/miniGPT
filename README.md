Local AI Chatbot (miniGPT) - Comprehensive Documentation

1. Introduction

The miniGPT project offers a straightforward, locally-operable AI chatbot solution, leveraging the power of LLaMA3 through Ollama. This system is designed for users who wish to run a large language model (LLM) directly on their machine without the need for external API keys or cloud services. It provides a private and self-contained environment for AI-driven conversational interactions.

2. Features

This project encompasses several key features that enhance its usability and accessibility:

•
Local Operation: The chatbot runs entirely on the user's local machine, ensuring data privacy and eliminating dependencies on external services.

•
LLaMA3 Integration: Utilizes the LLaMA3 large language model, facilitated by Ollama, to provide advanced conversational capabilities.

•
Conversation Memory: Maintains basic conversation history within the current session, allowing for more coherent and context-aware interactions.

•
Automated Setup: A dedicated setup script (run.py) automates the installation of necessary dependencies, Ollama, and the LLaMA3 model, streamlining the deployment process.

3. Architecture

The miniGPT system is composed of three primary components that work in concert to deliver the local AI chatbot functionality:

1.
Ollama: This component is responsible for hosting and running the LLaMA3 AI model locally. It exposes a local API (typically at http://localhost:11434 ) that allows other applications to interact with the AI model.

2.
Python Chatbot (miniGPT.py): This Python script serves as the user interface and the core logic for the chatbot. It handles sending user messages to the local Ollama API and processing the AI's responses for display. It also manages the conversation memory.

3.
Setup Script (run.py): This script is designed to automate the entire setup process. Its responsibilities include:

•
Verifying and installing required Python dependencies (e.g., requests).

•
Checking for and installing Ollama if it is not already present on the system.

•
Downloading the specified LLaMA3 model through Ollama.

•
Initiating the Ollama AI server.

•
Launching the miniGPT.py chatbot to begin user interaction.



4. Installation and Setup

To get the miniGPT chatbot up and running on your local machine, follow these steps:

4.1. Prerequisites

Ensure that Python 3 is installed on your system. You can verify its presence and version by running the following command in your terminal:

Bash


python3 --version



If Python 3 is not installed, you can install it on Ubuntu/Debian-based systems using:

Bash


sudo apt update
sudo apt install python3 python3-pip -y



4.2. Project Setup

1.
Clone the Repository: Begin by cloning the miniGPT GitHub repository to your local machine:

Bash









git clone https://github.com/faresQ7h/miniGPT.git
```

1.
Navigate to the Project Directory: Change your current directory to the newly cloned miniGPT project folder:

Bash









cd miniGPT
```

1.
Run the Setup Script: Execute the run.py script. This script will automatically handle all further installations and configurations, including Ollama and the LLaMA3 model, and then launch the chatbot.

Bash









python3 run.py
```

Plain Text


The `run.py` script performs the following actions:
*   Installs the `requests` Python library if missing.
*   Detects your operating system to install Ollama (currently supports Linux and Darwin/macOS ).
*   If Ollama is not detected, it will attempt to install it using `curl -fsSL https://ollama.com/install.sh | sh` for Linux/macOS.
*   It then pulls the `llama3` model using `ollama pull llama3`.
*   Finally, it starts the Ollama server and executes `miniGPT.py`.

*Note: If you are on an unsupported operating system or encounter issues with the automated Ollama installation, the script will prompt you to install Ollama manually from [https://ollama.com/download](https://ollama.com/download ).*



5. Usage

Once the run.py script has completed its setup and launched the chatbot, you will see a prompt in your terminal. You can then start typing your messages to interact with the LLaMA3 AI model. The chatbot will maintain a basic memory of your conversation within the current session.

To exit the chatbot, type exit and press Enter.

6. Contributing

Contributions to the miniGPT project are welcome. Please refer to the GitHub repository for guidelines on how to contribute, report issues, or suggest enhancements.

7. License

This project is open-source. Please refer to the LICENSE file in the repository for detailed licensing information. (Note: A LICENSE file was not explicitly found in the initial review, but it is good practice to include this section as a placeholder.)

