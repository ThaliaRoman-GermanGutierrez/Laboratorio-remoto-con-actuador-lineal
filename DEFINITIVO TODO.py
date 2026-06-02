import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib  # Importamos la librería del motor paso a paso

# --- CONFIGURACIÓN DE PINES ---
BOMBA_PIN = 4
IN1 = 22
IN2 = 27
SENSOR_PIN = 23  # Pin de señal final de carrera

# Pines del motor paso a paso lineal
GPIO_pins = (6, 13)  # Pines de (MS1, MS2)
direction = 26       # Pin de dirección
step = 19            # Pin de los pasos

# --- CONFIGURACIÓN INICIAL DE GPIO ---
GPIO.setmode(GPIO.BCM)
GPIO.setup([BOMBA_PIN, IN1, IN2], GPIO.OUT)
GPIO.setup(SENSOR_PIN, GPIO.IN)

# --- INSTANCIA DEL MOTOR PASO A PASO ---
mymotortest = RpiMotorLib.A3967EasyNema(direction, step, GPIO_pins)

# --- FUNCIONES DE CONTROL ---
def prender_bomba():
    print("Bomba: ENCENDIDA")
    GPIO.output(BOMBA_PIN, GPIO.HIGH)

def apagar_bomba():
    print("Bomba: APAGADA")
    GPIO.output(BOMBA_PIN, GPIO.LOW)

def arriba():
    print("Motor Principal: ADELANTE (Subiendo)")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

def abajo():
    print("Motor Principal: ATRÁS (Bajando)")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

def detener_motor():
    print("Motor Principal: DETENIDO")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

def detener_todo():
    GPIO.output(BOMBA_PIN, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    print("\nTodo el sistema se ha detenido de forma segura.")

# --- BUCLE PRINCIPAL ---
try:
    print("Sistema iniciado. Presiona Ctrl+C para detener todo.")
    
    while True:
        # --- PASO 1: BAJAR MOTOR VERTICAL DE FORMA DEFINITIVA ---
        
        time.sleep(1)
        prender_bomba()
        abajo()
        print("Bajando... Esperando a que llegue al tope.")
        
        # El motor bajará continuamente MIENTRAS el sensor lea HIGH (No tocado)
        while GPIO.input(SENSOR_PIN) == GPIO.HIGH:
            time.sleep(0.01)
            
        # --- PASO 2: ACCIÓN AL TOCAR EL SENSOR ---
        
        print("¡Sensor activado! Pieza detectada.")
        detener_motor()
        time.sleep(1)
        print("Esperando 1 segundo quieto...")
        time.sleep(1)
        
        # --- PASO 3: SUBIR MOTOR CON BOMBA AGARRADA ---
        
        print("Subiendo estrictamente por 20.5 segundos...")
        arriba()
        time.sleep(20.5)
        detener_motor()
        time.sleep(3)
        
        # --- PASO 4: MOVER MOTOR LINEAL A POSICION B ---
        
        print(">>> MOTOR LINEAL: ARRANCANDO (En paralelo con subida)")
        mymotortest.motor_move(.005, 2700, True, True, "Full", .05)
        print(">>> MOTOR LINEAL: PARADO")
        
        # --- PASO 5: BAJAR MOTOR VERTICAL DE FORMA DEFINITIVA  ---
        
        time.sleep(3)
        abajo()
        apagar_bomba()
        # El motor bajará continuamente MIENTRAS el sensor lea HIGH (No tocado)
        print("Bajando... Esperando a que el sensor cambie de estado.")
        while GPIO.input(SENSOR_PIN) == GPIO.HIGH:
            time.sleep(0.01)
        prender_bomba()
        
        # --- PASO 6: ACCIÓN AL TOCAR EL SENSOR ---
        
        print("¡Sensor activado! Pieza detectada.")
        detener_motor()
        apagar_bomba()
        time.sleep(1)
        print("Esperando 1 segundo quieto...")
        time.sleep(1)
        
        # --- PASO 7: SUBIR MOTOR CON BOMBA SUELTA ---
        
        print("Subiendo estrictamente por 20.5 segundos...")
        arriba()
        time.sleep(20.5)
        detener_motor()
        time.sleep(3)
               
        # --- PASO 8: EMPIEZA MOVIMIENTO A LA POSICION ORIGINAL ---
        
        print(">>> MOTOR LINEAL: REGRESANDO AL ORIGEN")
        mymotortest.motor_move(.005, 2700, False, True, "Full", .05)
        print(">>> MOTOR LINEAL: CICLO COMPLETADO")
        
        # --- PASO 9: FINALIZACION DE CICLO ---
        
        print("Ciclo completado. Volviendo a bajar...\n")
        time.sleep(4)  # Tiempo de espera antes de volver a empezar el ciclo

except KeyboardInterrupt:
    detener_todo()
finally:
    GPIO.cleanup()