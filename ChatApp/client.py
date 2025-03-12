import socket
import threading


def chat(peer_socket, recipient):
    def receive_messages():
        while True:
            try:
                message = peer_socket.recv(1024).decode("utf-8")
                if not message:
                    break
                print(f"\r{recipient}: {message}\nYou: ", end="")
            except:
                break
        peer_socket.close()

    threading.Thread(target=receive_messages, daemon=True).start()

    while True:
        message = input("You: ")
        if message.lower() == "exit":
            break
        peer_socket.send(message.encode("utf-8"))

    peer_socket.close()



def client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8095))

    username = input("Enter your username: ").strip()
    client.send(username.encode("utf-8"))

    recipient = input("Enter username to chat with: ").strip()
    client.send(recipient.encode("utf-8"))

    response = client.recv(1024).decode("utf-8")

    if response == "CONNECT":
        print(f"Connected to {recipient}. Start chatting!\n")
        chat(client, recipient)
    else:
        print("User not found.")
        client.close()


client()
