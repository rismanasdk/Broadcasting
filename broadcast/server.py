import socket
import threading

client = []

def broadcast(pesan, pengirim):
    for clienst in client:
        if clienst != pengirim:
            try:
                clienst.sendall(pesan.encode())
            except:
                client.remove(clienst)



def handle_client(conn, addr):
    print(f"[+] Client Terhubung {addr}")
    client.append(conn)
    print(f"Total Client :{len(client)}")

    while True:
        dataClient = conn.recv(1024)

        if not dataClient:
            break

        pesan = dataClient.decode()

        if pesan == "exit":
            conn.close()
            break

        print(f"{addr} :{pesan}")
        broadcast(f"{addr} :{pesan}", conn)

    client.remove(conn)
    conn.close()
    print(f"[-] Client Keluar {addr}")
    print(f"Total Client :{len(client)}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((socket.gethostbyname(socket.gethostname()), 9999))
server.listen(5)

print("Menunggu Client...")

while True:
    conn, addr = server.accept()
    threading.Thread(
        target=handle_client,
        args=(conn, addr)
    ).start()