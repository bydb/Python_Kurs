from djitellopy import Tello
import time

# Verbindung zur Drohne herstellen
tello = Tello()
tello.connect()

print(f"Batterie: {tello.get_battery()}%")

# Starten des Flugs
tello.takeoff()

# Vierecksflug
def fly_square(length):
    for i in range(4):
        tello.move_forward(length)  # Kantenlänge ist 30 cm
        tello.rotate_clockwise(90)   # Da es ein Viereck ist, drehen wir uns nach jedem Schritt um 90 Grad im Uhrzeigersinn

fly_square(30)  # Starten des Vierecksflugs mit Kantenlänge von 30 cm

# Landen der Drohne
tello.land()