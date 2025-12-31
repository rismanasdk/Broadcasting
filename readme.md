# Simple Python TCP Chat Broadcast

A simple real-time chat application using Python's `socket` and `threading` libraries. This project allows multiple clients to connect to a central server and broadcast messages to each other in real-time.

---

## Features
- **Multi-client Support**: Allows multiple users to join the chat simultaneously.
- **Real-time Broadcasting**: Every message sent by a client is broadcasted to all other active connections.
- **Concurrent Handling**: Uses `threading` to manage each client connection independently without blocking the server.
- **Safe Disconnection**: Includes an `exit` command to safely close client-server connections.
- **Dynamic IP Binding**: The server automatically detects and binds to the local host's IP address.

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: 
  - `socket`: For low-level network interface.
  - `threading`: For handling multiple client processes concurrently.

---

## How to Run

### 1. Prerequisites
- Ensure you have **Python 3** installed on your machine.
- Both the server and clients must be connected to the **same local network (LAN/Wi-Fi)**.

### 2. Configure the Client
Before running, open `client.py` and ensure the IP address in `client.connect()` matches the **Server's IP address**.
```python
# In client.py
client.connect(("SERVER_IP_ADDRESS", 9999))
