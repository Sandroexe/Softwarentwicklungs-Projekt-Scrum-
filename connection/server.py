import socket

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 65432        # Ein freier Port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server gestartet. Warte auf Verbindung auf Port {port}...")
        
        conn, addr = s.accept() 
        with conn:
            print(f"Erfolgreich verbunden mit: {addr}")
            conn.sendall(b"Willkommen beim Schach-Server!")

# NEU: Diese Zeilen sorgen dafür, dass die Funktion startet, 
# wenn du diese Datei direkt ausführst.
if __name__ == "__main__":
    start_server()