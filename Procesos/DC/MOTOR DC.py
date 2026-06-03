# - PROGRAMACION DE MOTOR DC -

import RPi.GPIO as GPIO
from time import sleep

# - CONFIGURACION DE PINES -

IN1 = 22
IN2 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# - DEFINICIONES DEL MOTOR, SUBE Y BAJA -

def baja(): #MOTOR BAJANDO 
    print("Motor DC: Bajando") # IMPRESION EN CONSOLA 
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

def sube(): #MOTOR SUBIENDO 
    print("Motor DC: Subiendo")  # IMPRESION EN CONSOLA 
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

# - DETECCION DEL MOTOR - 

def detener(): #APAGADO DEL MOTOR
    print("Motor detenido")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

# - SISTEMA CONTINUO DEL MOTOR DC - 

try:
    while True:
        
        baja() #BAJA EL MOTOR 
        sleep(10) #TIEMPO DE ESPERA 
        sube() # SUBE EL MOTOR 
        sleep(10) # tIEMPO DE ESPERA 
        detener() # dETIENE EL MOTOR 
    
except KeyboardInterrupt: #DETECCION DE TODO 
    detener_todo()
    
finally: #LIMPIEZA CODIGO
    GPIO.cleanup()   


