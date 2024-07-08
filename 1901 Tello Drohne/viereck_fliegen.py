from djitellopy import Tello
import time

# Erstelle eine Instanz der Tello-Klasse
tello = Tello()

# Verbinde mit der Tello-Drohne
tello.connect()

# Gebe den Batteriestand der Drohne aus
print(f"Batteriestand: {tello.get_battery()}%")

# Starten der Drohne
tello.takeoff()

# Warte eine Sekunde um sicherzustellen, dass die Drohne stabil ist
time.sleep(1)

# Definiere die Kantenlänge des Vierecks in cm
edge_length = 30

# Fliege das Viereck
for _ in range(4):
    tello.move_forward(edge_length)
    tello.rotate_clockwise(90)

# Landen der Drohne
tello.land()

# Verbindung trennen
tello.end()