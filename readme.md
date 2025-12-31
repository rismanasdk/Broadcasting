# Simple Python TCP Chat Broadcast

A simple real-time chat application using Python's `socket` and `threading` libraries. This project allows multiple clients to connect to a central server and broadcast messages to each other.

## Features
- **Multi-client Support**: Multiple users can join the chat simultaneously.
- **Real-time Broadcasting**: Messages sent by one client are delivered to all other connected clients.
- **Threading**: Handles each client connection on a separate thread for smooth interaction.
- **Exit Command**: Simple `exit` command to disconnect safely.

## How to Run

### 1. Prerequisite
- Make sure you have Python installed.
- Ensure both Server and Client are on the same network.

### 2. Run the Server
Open your terminal and run:
```bash
python server.py
