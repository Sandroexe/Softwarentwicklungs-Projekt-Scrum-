import socket


def connect_to_server():
    """Verbindet sich mit dem Schach-Server und empfängt eine Antwort."""
    # Der Nutzer muss die IP-Adresse des Servers eingeben.
    host = input("Gib die IP-Adresse des Servers ein: ")
    port = 65432

    try:
        # Öffnet einen TCP-Socket und sorgt dafür, dass er am Ende geschlossen wird.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"Versuche mit {host} zu verbinden...")
            s.connect((host, port))

            # Empfängt bis zu 1024 Bytes vom Server.
            data = s.recv(1024)
            print(f"Antwort: {data.decode('utf-8')}")
    except Exception as e:
        # Bei jeder Art von Verbindungsfehler wird diese Meldung ausgegeben.
        print(f"Fehler: Verbindung konnte nicht hergestellt werden.\n{e}")


if __name__ == "__main__":
    # Führt die Verbindungsfunktion nur aus, wenn das Skript direkt gestartet wird.
    connect_to_server()
