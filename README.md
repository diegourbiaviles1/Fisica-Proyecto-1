## Descripcion General
El programa permite a los usuarios posicionar múltiples cargas fuente y una carga objetivo para observar el comportamiento de los campos de fuerza mediante una interfaz gráfica dinámica.

### Caracteristicas Principales:
* Simulacion en Tiempo Real: Visualización de vectores de fuerza individuales y neta.
* Motor Fisico Preciso: Basado en la Ley de Coulomb y el Principio de Superposición.
* Interfaz Intuitiva: Paneles de control para entrada de datos y gestión de cargas.
* Auto-Escalado: El plano cartesiano se ajusta automáticamente para mantener todas las cargas visibles.

---

## Tecnologias y Librerias
El proyecto está desarrollado íntegramente en Python, utilizando las siguientes librerías estándar:

* Tkinter: Para la creación de la interfaz gráfica y el motor de dibujo (Canvas).
* Math: Para el cálculo de raíces cuadradas, distancias y funciones trigonométricas.
* Messagebox: Para la gestión de validación de datos y errores de usuario.
* TTK: Para la mejora de la jerarquía visual de los componentes.

---

## Logica y Funciones de Fisica
La lógica científica se encuentra centralizada en el archivo Fisica.py:

### 1. calcular_fuerza_vector
Calcula la interacción entre dos partículas específicas.
* Distancia: Calculada mediante el teorema de Pitágoras.
* Descomposicion: La fuerza se separa en componentes Fx y Fy usando vectores unitarios para mantener la precisión direccional.
* Validacion: El código previene errores de división entre cero si las cargas coinciden en posición.

### 2. calcular_fuerza_neta
Aplica el Principio de Superposición.
* Iteracion: Recorre todas las cargas fuente almacenadas en el sistema.
* Suma Vectorial: Acumula las fuerzas resultantes de cada interacción para entregar la magnitud y ángulo total.

---

## Integrantes
* Diego Armando Urbina Avilés
* Emmanuel Leonardo Aguilar Novoa
* Jose Francisco Lopez Mayorga

---

Proyecto desarrollado para la asignatura de Física Aplicada - Universidad Americana (UAM).
