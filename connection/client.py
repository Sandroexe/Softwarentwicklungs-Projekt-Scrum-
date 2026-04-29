import socket

def connect_to_server():
    host = '127.0.0.1'  
    port = 65432        

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Versuche mit Server {host}:{port} zu verbinden...")
        s.connect((host, port))
        
        data = s.recv(1024)
        print(f"Nachricht vom Server empfangen: {data.decode('utf-8')}")

# NEU: Auch hier der direkte Startbefehl
if __name__ == "__main__":
    connect_to_server()