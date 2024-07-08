from djitellopy import Tello
import time
import cv2

# Erstelle eine Instanz der Tello-Klasse
tello = Tello()

# Verbinde mit der Tello-Drohne
tello.connect()

# Gebe den Batteriestand der Drohne aus
print(f"Batteriestand: {tello.get_battery()}%")

# Starte den Video-Stream
tello.streamon()

# Starten der Drohne
tello.takeoff()

# Warte eine Sekunde, um sicherzustellen, dass die Drohne stabil ist
time.sleep(1)

# Definiere die Kantenlänge des Vierecks in cm
edge_length = 30

# Fliege das Viereck und mache Fotos an den Wendepunkten
for i in range(4):
    # Bewege die Drohne nach vorne
    tello.move_forward(edge_length)

    # Mache ein Foto
    frame_read = tello.get_frame_read()
    frame = frame_read.frame
    cv2.imwrite(f'photo_{i+1}.jpg', frame)
    print(f'Foto {i+1} gemacht und gespeichert.')

    # Drehe die Drohne um 90 Grad im Uhrzeigersinn
    tello.rotate_clockwise(90)

# Landen der Drohne
tello.land()

# Beende den Video-Stream
tello.streamoff()

# Verbindung trennen
tello.end()