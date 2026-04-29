import tkinter as tk
from tkinter import messagebox
from connection.server import start_server
from connection.client import connect_to_server


def starte_server():
    """Startet den Server."""
    fenster.destroy()
    start_server()


def starte_client():
    """Startet den Client."""
    fenster.destroy()
    connect_to_server()


# Fenster erstellen
fenster = tk.Tk()
fenster.title("SCHACH - Modus Auswahl")
fenster.geometry("300x200")
fenster.resizable(False, False)

# Titel
titel = tk.Label(fenster, text="SCHACH", font=("Arial", 24, "bold"))
titel.pack(pady=20)

# Untertitel
untertitel = tk.Label(fenster, text="Wähle deinen Modus", font=("Arial", 12))
untertitel.pack(pady=10)

# Button-Rahmen
button_rahmen = tk.Frame(fenster)
button_rahmen.pack(pady=20)

# Server Button
button_server = tk.Button(
    button_rahmen,
    text="🖥️ Server",
    command=starte_server,
    width=15,
    height=2,
    font=("Arial", 11),
    bg="#4CAF50",
    fg="white"
)
button_server.pack(pady=10)

# Client Button
button_client = tk.Button(
    button_rahmen,
    text="👤 Client",
    command=starte_client,
    width=15,
    height=2,
    font=("Arial", 11),
    bg="#2196F3",
    fg="white"
)
button_client.pack(pady=10)

# Fenster anzeigen
fenster.mainloop()
