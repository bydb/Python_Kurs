import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.positioning.motion_commander import MotionCommander

# Initialisierung der Treiber
cflib.crtp.init_drivers()

# URI Ihrer Crazyflie
URI = 'radio://0/80/2M'

# Hauptprogramm
if __name__ == '__main__':
    # Erstellen einer Crazyflie-Instanz
    cf = Crazyflie(rw_cache='./cache')

    # Verbindung herstellen
    print('Verbinden mit {}'.format(URI))
    cf.open_link(URI)

    # Warten, bis die Verbindung hergestellt ist
    time.sleep(1)

    with MotionCommander(cf, default_height=0.5) as mc:
        # Seitenlänge in Metern
        side_length = 0.3

        # Quadrat fliegen
        for _ in range(4):
            mc.forward(side_length)
            mc.turn_right(90)

        # Kurze Pause
        time.sleep(1)

    # Verbindung schließen
    cf.close_link()