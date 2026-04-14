import os
import platform
import subprocess
import sys
import time
import socket
import atexit

print("🚀 Starting setup...")

os_name = platform.system()
print(f"Detected OS: {os_name}")

# -------- INSTALL REQUESTS --------
try:
    import requests
    print("✅ requests already installed")
except ImportError:
    print("📦 Installing requests...")
    subprocess.run([sys.executable, "-m", "pip", "install", "requests"])

# -------- CHECK OLLAMA --------
def is_ollama_installed():
    try:
        subprocess.run(["ollama", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False

if not is_ollama_installed():
    print("📦 Installing Ollama...")
    if os_name in ["Linux", "Darwin"]:
        subprocess.run("curl -fsSL https://ollama.com/install.sh | sh", shell=True)
    else:
        print("⚠️ Install Ollama manually: https://ollama.com/download")
        sys.exit()
else:
    print("✅ Ollama already installed")

# -------- CHECK IF RUNNING --------
def is_ollama_running():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(("127.0.0.1", 11434))
        s.close()
        return True
    except:
        return False

ollama_process = None
started_by_script = False

if not is_ollama_running():
    print("⚡ Starting Ollama...")
    ollama_process = subprocess.Popen(["ollama", "serve"])
    started_by_script = True
    time.sleep(5)
else:
    print("✅ Ollama already running")

# -------- CLEAN SHUTDOWN --------
def cleanup():
    if started_by_script and ollama_process:
        print("\n🛑 Stopping Ollama...")
        ollama_process.terminate()
        try:
            ollama_process.wait(timeout=3)
        except:
            ollama_process.kill()

atexit.register(cleanup)

# -------- CHECK MODEL --------
print("🧠 Checking model...")
result = subprocess.run(["ollama", "list"], capture_output=True, text=True)

if "llama3" not in result.stdout:
    print("⬇️ Downloading llama3...")
    subprocess.run(["ollama", "pull", "llama3"])
else:
    print("✅ llama3 already available")

# -------- RUN CHAT --------
if not os.path.exists("miniGPT.py"):
    print("❌ miniGPT.py not found")
    sys.exit()

print("\n🤖 Launching chatbot...\n")

try:
    subprocess.run([sys.executable, "miniGPT.py"])
except KeyboardInterrupt:
    print("\nInterrupted by user")