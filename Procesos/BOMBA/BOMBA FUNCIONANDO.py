# - PROGRAMACION DE LA BOMBA -

import RPi.GPIO as GPIO
import time 

# - CONFIGURACION DEL PIN -

BOMBA_PIN = 4 

GPIO.setmode(GPIO.BCM)
GPIO.setup(BOMBA_PIN, GPIO.OUT)

# - DEFINICIONES DE ENECENDIOD Y APAGADO -

def prender_bomba():
    print("Bomba encendida") # IMPRESION EN CONSOLA  
    GPIO.output(BOMBA_PIN, GPIO.HIGH) # ENCENDIDO DE LA BOMBA 

def apagar_bomba():
    print("Bomba apagada") # IMPRESION EN CONSOLA 
    GPIO.output(BOMBA_PIN, GPIO.LOW) # APAGADO DE LA BOMBA 

# - SISTEMA CONTINUO DEL FUNCIONAMIENTO -
try:
    
    while True:

        prender_bomba() # ENCIENDE LA BOMBA
        time.sleep(5) # TIEMPO DE ESPERA
        
        apagar_bomba() # APAGADO DE LA BOMBA
        time.sleep(5) #TIEMPO DE ESPERA 

except KeyboardInterrupt: #DETECCION DE TODO 
    detener_todo()
    
finally: # lIMPIEZA DE CODIGO
    GPIO.cleanup()