# server.py

print("starting Server...")

import socket

def start_server():
    host = '127.0.0.1'  # Localhost (dein eigener PC)
    port = 65432        # Ein freier Port

    # Erstellt einen IPv4 (AF_INET) TCP (SOCK_STREAM) Socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server gestartet. Warte auf Verbindung auf Port {port}...")
        
        # Blockiert das Skript, bis ein Client sich verbindet
        conn, addr = s.accept() 
        with conn:
            print(f"Erfolgreich verbunden mit: {addr}")
            # Sendet eine kurze Testnachricht an den Client
            conn.sendall(b"Willkommen beim Schach-Server!")