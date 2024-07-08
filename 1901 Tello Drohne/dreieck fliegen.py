from djitellopy import Tello
import cv2
import time

tello = Tello()
tello.connect()
print(tello.get_battery())

tello.takeoff()
time.sleep(1)
kantenlaenge = 40

# Fly triangle and take pictures
for _ in range(3):
    tello.move_forward(kantenlaenge)  # Move forward 90 units
    tello.rotate_counter_clockwise(120)  # Rotate counter-clockwise by 120 degrees

tello.land()