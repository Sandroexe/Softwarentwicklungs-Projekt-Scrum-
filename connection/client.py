# client.py

print("starting Client...")

import socket

def connect_to_server():
    host = '127.0.0.1'  # Die IP des Servers (hier wieder dein eigener PC)
    port = 65432        # Muss exakt der gleiche Port wie beim Server sein

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Versuche mit Server {host}:{port} zu verbinden...")
        s.connect((host, port))
        
        # Wartet auf eine Nachricht vom Server (max 1024 Bytes)
        data = s.recv(1024)
        
        # Die empfangenen Bytes wieder in einen Text (String) umwandeln
        print(f"Nachricht vom Server empfangen: {data.decode('utf-8')}")