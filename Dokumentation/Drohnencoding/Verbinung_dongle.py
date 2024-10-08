import cflib.crtp

# Initialisieren der Treiber
cflib.crtp.init_drivers()

# Suchen nach verfügbaren Crazyflies
available = cflib.crtp.scan_interfaces()
print('Verfügbare Crazyflies:')
for i in available:
    print(i[0])
    