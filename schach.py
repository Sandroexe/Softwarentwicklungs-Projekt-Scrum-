# schach.py

print("starte schach.py...")

from gui.menu import zeige_menu
from connection.server import start_server
from connection.client import connect_to_server

# GUI Menu anzeigen und Auswahl entgegennehmen
modus = zeige_menu()

# Basierend auf der Auswahl den entsprechenden Modus starten
if modus == "server":
    print("→ Starte SERVER...")
    start_server()
elif modus == "client":
    print("→ Starte CLIENT...")
    connect_to_server()
else:
    print("Keine Auswahl getroffen!")

