# - PROGRAMACION DE TODO LAS PLACAS UNIDAS -
import RPi.GPIO as GPIO
import time 
from RpiMotorLib import RpiMotorLib

# - CONFIGURACIÓN DE PINES -

BOMBA_PIN = 4 
IN1 = 22
IN2 = 27

# - PINES DEL MOTOR PASO A PASO LINEAL -

GPIO_pins = (6, 13) 
direction = 26      
step = 19           

# - CONFIGURACIÓN INICIAL GPIO -

GPIO.setmode(GPIO.BCM)
GPIO.setup([BOMBA_PIN, IN1, IN2], GPIO.OUT)

# - INSTANCIA DEL MOTOR LINEAL PASO A PASO -

mymotortest = RpiMotorLib.A3967EasyNema(direction, step, GPIO_pins)

# - DEFINCIIONES DE LAS DIFERENTES FUNCIONES -

def prender_bomba(): # ENCENDIO DE LA BOMBA 
    print("Bomba: ENCEDIDA") # IMPRESION EN CONSOLA 
    GPIO.output(BOMBA_PIN, GPIO.HIGH)

def apagar_bomba(): # APAGADO DE LA BOMBA 
    print("Bomba: APAGADA") # IMPRESION EN CONSOLA 
    GPIO.output(BOMBA_PIN, GPIO.LOW)

def baja(): # MOTOR BAJANDO 
    print("Motor DC: Bajando") # IMPRESION EN CONSOLA 
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

def sube(): # MOTOR SUBIENDO 
    print("Motor DC: Subiendo") # IMPRESION EN CONSOLA 
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

def detener_motor(): # DETECCION DEL MOTOR DC
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

def detener_todo(): # DETECCION DE TODO EL SISTEMA 
    GPIO.output(BOMBA_PIN, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    print("\nTodo el sistema se ha detenido de forma segura.") # IMPRESION EN CONSOLA 

# - BUCLE PRINCIPAL -
try:
    print("Sistema iniciado. Presiona Ctrl+C para detener todo.") # IMPRESION EN CONSOLA 
    while True:
        print("\n--- INICIO DE CICLO ---")# IMPRESION EN CONSOLA  
        time.sleep(5) # TIEMPO DE ESPERA  

# - PROCESO INICIAL -

    # - RECOLECCION DEL PING PONG -
    
        prender_bomba() # ENECENDIO DE LA BOMBA PARA LA RECOLECCION DEL PING PONG 
        time.sleep(2) # TIEMPO DE ESPERA
        baja() # BAJA EL MOTOR PARA GENERAR PRESION AL PING PONG 
        time.sleep(15) # DURACION DE MOTOR BAJANDO
        detener_motor() # DETECCION DEL MOTOR DC
        time.sleep(5) # TIEMPO DE ESPERA 
        sube() # SUBE EL MOTOR DESPUES DE OBTENER EL PING PONG 
        time.sleep(15) # TIEMPO DEL MOTOR EN MOVIMIENTO 
        detener_motor() # DETECCION DEL MOTOR 
        print("Ping pong recogido. Iniciando trayecto") # IMPRESION EN CONSOLA
        time.sleep(5) # TIEMPO DE ESPERA
        
# - PROCESO INTERMEDIO -

    # - TRASLADO DEL PING PONG -
        
        print(">>> MOTOR LINEAL: TRANSPORTANDO  (Ida)") # IMPRESION EN CONSOLA 
        mymotortest.motor_move(.005, 3100, True, True, "Full", .05) # MOVIMIENTO DE DERECHA A IZQUIERDA, TRASLADANDO DEL PING PONG 
        print(">>> MOTOR LINEAL: PARADO / ESPERANDO")# IMPRESION EN CONSOLA  
        time.sleep(2) # TIEMPO DE ESPERA 

    # - EXPULSAR PING PONG -
        
        baja() # BAJA EL MOTOR PARA GENERAR PRECISION AL EXPULSAR EL PING PONG 
        time.sleep(15) # DURACION DE MOTOR BAJANDO
        detener_motor() # DETECCION DEL MOTOR DC
        time.sleep(5) # TIEMPO DE ESPERA
        apagar_bomba() # APAGADO DE LA BOMBA PARA SOLTAR EL PING PONG
        time.sleep(2) # TIEMPO DE ESPERA
        sube() # SUBE EL MOTOR DESPUES DE SOLTAR EL PING PONG 
        time.sleep(15) # TIEMPO DEL MOTOR EN MOVIMIENTO 
        detener_motor() # DETECCION DEL MOTOR     
        print("Ping pong expulsado. Regresando al trayecto")
        time.sleep(5)   
          
# - PROCESO FINAL -

    # - TRASLADO DEL MOTOR PASO A PASO PARA RECOLECCION DE OTRO PING PONG -  
        
        print(">>> MOTOR LINEAL: REENCENDIDO (Regresando)") # IMPRESION EN CONSOLA 
        mymotortest.motor_move(.005, 3100, False, True, "Full", .05) # MOVIMIENTO DE IZQUIERDA A DERECHA 
        
        
# FINAL DEL CICLO

    # - DETECCION DE TODO EL SISTEMA -
    
        detener_todo() # SISTEMA DETENIDO 
        print(">>> CICLO COMPLETO FINALIZADO") # IMPRESION EN CONSOLA 
        time.sleep(20) # TIEMPO DE ESPERA 

except KeyboardInterrupt: # DETECCION POR COMANDO 
    detener_todo()

finally: # LIMPIEZA DE GPIO 
    GPIO.cleanup()