from djitellopy import Tello
import time
tello = Tello()
tello.connect()
print(tello.get_battery())

tello.takeoff()
tello.curve_xyz_speed(x1=90, y1=0, z1=0, x2=0, y2=-90, z2=0, speed=60, time=3)
tello.curve_xyz_speed(x1=0, y1=90, z1=0, x2=-90, y2=0, z2=0, speed=60, time=3)
tello.land()