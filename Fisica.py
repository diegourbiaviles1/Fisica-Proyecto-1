import math

K = 8.99e9  # Constante de Coulomb en N·m²/C²

def calcular_fuerza_vector(q_fuente, pos_fuente, q_objetivo, pos_objetivo):
    dx = pos_objetivo[0] - pos_fuente[0]
    dy = pos_objetivo[1] - pos_fuente[1]

    r = math.sqrt(dx**2 + dy**2)

    if r == 0:
        raise ValueError("Dos cargas no pueden estar en la misma posición.")

    r_hat_x = dx / r   # componente x del vector unitario
    r_hat_y = dy / r   # componente y del vector unitario

    F_magnitud = K * q_fuente * q_objetivo / r**2

    Fx = F_magnitud * r_hat_x
    Fy = F_magnitud * r_hat_y

    return Fx, Fy

def calcular_fuerza_neta(cargas_fuente, posiciones_fuente, q_objetivo, pos_objetivo):
    Fx_neta = 0.0
    Fy_neta = 0.0
    fuerzas_individuales = []

    for i in range(len(cargas_fuente)):
        Fx, Fy = calcular_fuerza_vector(
            cargas_fuente[i], posiciones_fuente[i],
            q_objetivo, pos_objetivo
        )
        fuerzas_individuales.append((Fx, Fy))
        Fx_neta += Fx
        Fy_neta += Fy

    magnitud = math.sqrt(Fx_neta**2 + Fy_neta**2)

    return Fx_neta, Fy_neta, magnitud, fuerzas_individuales