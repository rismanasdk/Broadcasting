import socket
import threading

def terima_pesan():
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            print(f"\nDari Client lain :{data.decode()}")
        except:
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.0.9", 9999))

threading.Thread(target=terima_pesan, daemon=True).start()

while True:
    pesan = input("Pesan: ")

    if pesan == "exit":
        client.sendall(pesan.encode())
        break

    client.sendall(pesan.encode())

client.close()