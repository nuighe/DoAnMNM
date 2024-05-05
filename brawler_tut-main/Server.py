import socket
import threading

PORT = 55000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        try:
            msg = conn.recv(30).decode(FORMAT)
            print(f"[{addr}] {msg}")
            if msg[12:12+len(DISCONNECT_MESSAGE)] == DISCONNECT_MESSAGE:
                clients.remove(conn)
                print(f"[{addr}]----end-----")
                break

            for remote_client in clients:
                if remote_client != conn:
                    remote_client.send(msg.encode(FORMAT))

        except:
            clients.remove(conn)
            print(f"[{addr}]----end-----")
            break

    conn.close()

def start():
    server.listen(1)
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

print("[STARTING] Server is starting...")
start()
