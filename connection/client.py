import socket

def connect_to_server():
    # Jetzt fragen wir den User nach der IP des Servers
    host = input("Gib die IP-Adresse des Servers ein: ")
    port = 65432        

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"Versuche mit {host} zu verbinden...")
            s.connect((host, port))
            
            data = s.recv(1024)
            print(f"Antwort: {data.decode('utf-8')}")
    except Exception as e:
        print(f"Fehler: Verbindung konnte nicht hergestellt werden.\n{e}")

if __name__ == "__main__":
    connect_to_server()