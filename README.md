
# Sistema Mecatrónico de Bajo Costo para Laboratorio Remoto

## Descripción General

Este proyecto corresponde al desarrollo de un sistema mecatrónico de bajo costo orientado a laboratorios remotos de programación y automatización. El sistema permite manipular una pelota de ping pong mediante una bomba de succión controlada electrónicamente y un mecanismo de posicionamiento cartesiano de dos ejes (X-Z).

La plataforma utiliza una Raspberry Pi 4 como unidad principal de procesamiento y control, encargada de ejecutar scripts desarrollados en Python para coordinar el funcionamiento de los diferentes actuadores, sensores y módulos electrónicos.

El objetivo principal es proporcionar una herramienta educativa que permita comprender conceptos relacionados con programación, control de motores, electrónica digital y sistemas mecatrónicos mediante una experiencia práctica y remota.

---

## Arquitectura del Sistema

El sistema está compuesto por cuatro módulos principales:

### Unidad de Control

La Raspberry Pi 4 ejecuta los scripts de control y administra las señales de entrada y salida necesarias para el funcionamiento del sistema.

### Sistema de Posicionamiento Horizontal (Eje X)

Implementado mediante un motor paso a paso lineal controlado por el driver EasyDriver A3967. Este mecanismo permite desplazar la bomba de succión entre diferentes posiciones de trabajo.

### Sistema de Posicionamiento Vertical (Eje Z)

Implementado mediante un motorreductor DC controlado por un módulo L298N. Su función es acercar o alejar la bomba de la superficie de trabajo.

### Sistema de Succión

Compuesto por una bomba de vacío controlada mediante una tarjeta PCB diseñada específicamente para el proyecto. El accionamiento se realiza mediante un relé controlado desde la Raspberry Pi.

---

## Lógica de Funcionamiento

La operación completa del sistema se divide en las siguientes etapas:

1. Inicialización de GPIO y módulos de control.
2. Desplazamiento horizontal hacia la posición de captura.
3. Descenso vertical de la bomba.
4. Activación de la bomba de succión.
5. Elevación de la pelota.
6. Transporte horizontal hacia la posición destino.
7. Descenso para liberar el objeto.
8. Desactivación de la bomba.
9. Retorno a la posición inicial.
10. Detección del final de carrera.
11. Reinicio del ciclo.

---

## Módulos de Software

El desarrollo del sistema se realizó mediante scripts independientes para facilitar la validación individual de cada componente.

### Control de Bomba de Succión

Permite activar y desactivar el relé encargado de energizar la bomba mediante señales digitales provenientes de la Raspberry Pi.

### Control del Motor Paso a Paso

Genera las señales STEP y DIR necesarias para controlar el desplazamiento horizontal mediante el driver EasyDriver.

### Control del Motorreductor

Gestiona el movimiento ascendente y descendente mediante el puente H L298N.

### Lectura del Final de Carrera

Detecta la posición de referencia del sistema para garantizar ciclos repetitivos y seguros.

### Integración General

Coordina el funcionamiento de todos los módulos anteriores para ejecutar la secuencia completa de transporte.

---

## Características Técnicas

* Lenguaje de programación: Python.
* Sistema operativo: Raspberry Pi OS (Raspbian).
* Plataforma de desarrollo: Thonny IDE.
* Control mediante GPIO.
* Sistema de dos grados de libertad (X-Z).
* Supervisión visual mediante cámara Raspberry Pi.
* Arquitectura modular y escalable.
* Diseño orientado a laboratorios remotos educativos.

---

## Resultados

Las pruebas realizadas permitieron validar el funcionamiento individual de cada módulo y posteriormente la integración completa del sistema. Se verificó el control adecuado de la bomba de succión, el desplazamiento horizontal mediante motor paso a paso, el movimiento vertical mediante motorreductor y la detección correcta del sensor de final de carrera.

La integración de todos los componentes permitió ejecutar ciclos completos de captura, transporte y liberación de objetos de manera automática y repetitiva.
