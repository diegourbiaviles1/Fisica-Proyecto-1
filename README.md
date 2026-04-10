CALCULADORA DE FUERZA ELECTRICA

DESCRIPCION DEL PROYECTO
Este programa es una herramienta interactiva diseñada para calcular y visualizar la fuerza eléctrica neta que actúa sobre una carga objetivo debido a múltiples cargas fuente en un plano bidimensional. El sistema aplica los principios fundamentales de la electrostática para ofrecer tanto resultados numéricos precisos como una representación gráfica vectorial en tiempo real.


Captura y Validación: Recibe los datos del usuario (magnitud de carga en microculombios y posición en metros), validando que las entradas sean numéricas antes de procesarlas.

Motor de Cálculo: Utiliza el Principio de Superposición. Primero calcula la interacción individual entre cada carga fuente y la objetivo, y luego suma vectorialmente estas fuerzas para obtener el resultado neto.

Visualización Dinámica: Traduce las unidades del mundo físico (metros) a píxeles en pantalla mediante un sistema de escalado automático. Dibuja vectores proporcionales que indican la dirección y magnitud de las fuerzas mediante flechas orientadas trigonométricamente.

LIBRERIAS UTILIZADAS
El proyecto utiliza bibliotecas estándar de Python para garantizar portabilidad y eficiencia:

tkinter: Base para la interfaz gráfica de usuario y el lienzo de dibujo (Canvas).

messagebox: Gestión de alertas y errores de entrada.

math: Realización de cálculos complejos como raíces cuadradas, arcotangentes y funciones trigonométricas para el dibujo de vectores.

ttk: Utilizada para mejorar la estructura visual de los widgets de la interfaz.

FUNCIONES PRINCIPALES DE FISICA
Toda la lógica científica reside en el módulo Fisica.py:

calcular_fuerza_vector
Calcula la fuerza entre dos partículas siguiendo la Ley de Coulomb. Determina la distancia entre las cargas y descompone la fuerza en componentes X e Y utilizando vectores unitarios. Incluye una validación para evitar divisiones entre cero si las cargas están en la misma posición.

calcular_fuerza_neta
Implementa el Principio de Superposición. Itera a través de todas las cargas fuente almacenadas, acumula las componentes de fuerza de cada interacción y retorna la magnitud total junto con el desglose de fuerzas individuales para su visualización.



INTEGRANTES DEL PROYECTO
Diego Armando Urbina Avilés
Emmanuel Leonardo Aguilar Novoa
Jose Francisco Lopez Mayorga
