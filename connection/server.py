import socket

def get_ip_address():
    # Kleiner Trick: Erstellt eine Verbindung nach außen, um die eigene lokale IP zu sehen
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Die Ziel-IP muss nicht existieren, es geht nur um das Routing
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def start_server():
    host = '0.0.0.0'  # Akzeptiert Verbindungen von überall
    port = 65432
    
    mein_ip = get_ip_address()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"--- SCHACH SERVER ---")
        print(f"Deine lokale IP-Adresse: {mein_ip}")
        print(f"Warte auf Verbindung auf Port {port}...")
        
        conn, addr = s.accept() 
        with conn:
            print(f"Verbunden mit Client-IP: {addr[0]}")
            conn.sendall(b"Verbindung zum Schach-Server erfolgreich!")

if __name__ == "__main__":
    start_server()