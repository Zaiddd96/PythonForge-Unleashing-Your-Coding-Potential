import socket
import threading

clients = {}  # {username: socket}


def handle_client(client_socket, username):
    try:
        while True:
            recipient = client_socket.recv(1024).decode("utf-8").strip()
            if recipient in clients:
                recipient_socket = clients[recipient]
                client_socket.send(f"CONNECT".encode("utf-8"))
                recipient_socket.send(f"CONNECT".encode("utf-8"))
                private_chat(client_socket, recipient_socket)
            else:
                client_socket.send("ERROR:User not found.".encode("utf-8"))
    except:
        pass
    finally:
        remove_client(username)


def send_active_users(client_socket):
    users_list = ",".join(clients.keys())
    client_socket.send(f"USERS:{users_list}".encode("utf-8"))

def private_chat(client_socket, recipient_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            recipient_socket.send(message)
        except:
            break


def remove_client(username):
    if username in clients:
        clients[username].close()
        del clients[username]


def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8095))
    server.listen(5)
    print("Server is running on 0.0.0.0:8095")

    while True:
        client_socket, _ = server.accept()
        username = client_socket.recv(1024).decode("utf-8").strip()
        clients[username] = client_socket
        print(f"{username} is online.")
        threading.Thread(target=handle_client, args=(client_socket, username)).start()


server()
