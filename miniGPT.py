import requests
import textwrap

def format_response(text):
    """
    Make output cleaner (wrap text nicely)
    """
    return textwrap.fill(text, width=80)

print("\nSimple Local AI Chat")
print("-" * 30)
print("Type 'exit' to quit\n")

messages = []

while True:
    user_input = input("You > ")

    if user_input.lower() == "exit":
        print("\nBye.\n")
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "llama3",
                "messages": messages,
                "stream": False
            }
        )

        reply = response.json()["message"]["content"]

        print("\nAI >")
        print(format_response(reply))
        print("-" * 30)

        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("\n[Error] Could not reach AI.")
        print("Make sure Ollama is running.\n")