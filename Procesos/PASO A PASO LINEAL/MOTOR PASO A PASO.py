# -PROGRAMACION DE MOTOR PASO A PASO LINEAL -
import RPi.GPIO as GPIO
import time 
from RpiMotorLib import RpiMotorLib

#- CONFIGURACION DEL GPIO -

GPIO.setmode(GPIO.BCM)

# - CONFIGURACION DE PINES DEL MOTOR PASO A PASO LINEAL 

GPIO_pins = (6, 13) # PINES DE (MS1, MS2)
direction = 26      # PIN DE DIRECCION 
step = 19           # PIN DE LOS PASOS 

# - INSTANCIA DEL MOTOR PASO A PASO -

mymotortest = RpiMotorLib.A3967EasyNema(direction, step, GPIO_pins)

try:
    while True:
        
        # - EL MOTOR ARRANCA Y AVANZA (3100 PASOS DESDE EL PUNTO INICIAL) -
        
        print(">>> MOTOR LINEAL: ARRANCANDO")  # IMPRESION EN CONSOLA 
        mymotortest.motor_move(.005, 3100, True, True, "Full", .05) # GIRO DE DERECHA A IZQUIERA
        
        # - MOTOR SE DETIENE - 
        
        print(">>> MOTOR LINEAL: PARADO")  # IMPRESION EN CONSOLA 
        time.sleep(10)  # TIEMPO DE ESPERA 
        
        # - EL MOTOR AVANZA Y REGRESA AL ORIGEN (3100 PASOS DESDE EL PUNTO FINAL) -
        
        print(">>> MOTOR LINEAL: REGRESANDO") # IMPRESION EN CONSOLA
        mymotortest.motor_move(.005, 3100, False, True, "Full", .05) # GIRO DE IZQUIERDA A DERECHA
        
        # - EL MOTOR PASO A PASO TERMINA EL CICLO -
        
        print(">>> MOTOR LINEAL: CICLO COMPLETADO") # IMPRESION EN CONSOLA 
        time.sleep(2) # TIEMPO DE ESPERA 

# - APAGADO TOTAL DEL PROGRAMA -

except KeyboardInterrupt:
    print("\nDeteniendo programa...")

# - APAGADO DE LOS PINES -

finally: 
    GPIO.cleanup()