# CODIGO DE UNION DE BOMBA Y MOTOR DC 
import RPi.GPIO as GPIO
import time

#  CONFIGURACION DE LOS PINES

BOMBA_PIN = 4
IN1 = 22
IN2 = 27

# - CONFIGURACION DE LOS GPIO -

GPIO.setmode(GPIO.BCM)
GPIO.setup([BOMBA_PIN, IN1, IN2], GPIO.OUT)

# - DEFINICIONES DE LOS DIFERENTES PASOS -

def prender_bomba():  # ENCENDIDO DE LA BOMBA 
    print("Bomba: ENCEDIDA")  # IMPRESION DE CONSOLA 
    GPIO.output(BOMBA_PIN, GPIO.HIGH)

def apagar_bomba():
    print("Bomba: APAGADA") # IMPRESION DE CONSOLA
    GPIO.output(BOMBA_PIN, GPIO.LOW)

def adelante():
    print("Motor: ADELANTE") # IMPRESION DE CONSOLA
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

def atras():
    print("Motor: ATRÁS") # IMPRESION DE CONSOLA
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

def detener_todo(): 
    GPIO.output(BOMBA_PIN, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    print("\nTodo el sistema se ha detenido de forma segura.") # IMPRESION DE CONSOLA

def detener_motor():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    

try:
    print("Sistema iniciado. Presiona Ctrl+C para detener todo.") # INFORMACIO DE DETECCION 
    while True:
        print("Arranque de sistema") # IMPRESION DE CONSOLA
        time.sleep(1) # TIEMPO DE ESPERA
        
    # - PRIMER PROCESO - RECOLECCION DEL PING PONG 
    
        prender_bomba() # ENCIENDE LA BOMBA PARA EL PING PONG 
        time.sleep(1) # TIEMPO DE ESPERA 
        adelante() # EMPIEZA A DESENDER EL MOTOR CON LA BOMBA 
        time.sleep(25)  # TIEMPO DE ESPERA 
        detener_motor() # APAGA EL MOTOR 
        time.sleep(5) #TIEMPO DE ESPERA
        
    # - PROCESO DESPUES DE RECOGER EL PING PONG -
    
        adelante() # SUBE EL MOTOR CON LA BOMBA 
        time.sleep(15) # TIEMPO DE ESPERA         
        detener_motor() # APAGA EL MOTOR 
        time.sleep(10) # TIEMPO DE ESPERA
        
    # - DESPUES DEL MOVIMIENTO LINEAL HORIZONTAL -
    
        #apagar_bomba()  # APAGA LA BOMBA 
        time.sleep(5) # TIEMPO DE ESPERA 
        
    # - DETECCION DE TODO EL SISTEMA - 
        detener_todo() # DETIENE TODO DESPUES DE LOS CICLOS 
        time.sleep(5) # TIEMPO DE ESPERA 
 
except KeyboardInterrupt: # COMANDO DE DETECCION DE TODO 
    detener_todo()
finally: # FINALIZA LIMPIANDO EL GPIO
    GPIO.cleanup() 