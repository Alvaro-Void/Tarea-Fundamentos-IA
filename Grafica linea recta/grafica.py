# librerías para cálculos y gráfica
import numpy as np
import matplotlib.pyplot as plt

# genera la figura de la recta
def generar_grafica(m, b):
    # valores de x
    x = np.linspace(-10, 10, 100)

    # función lineal
    y = m * x + b

    # crear figura
    fig, ax = plt.subplots()

    # dibujar la recta
    ax.plot(x, y)

    # nombres de ejes
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # título
    ax.set_title(f"f(x) = {m}x + {b}")

    # líneas de referencia
    ax.axhline(0)
    ax.axvline(0)

    # cuadrícula
    ax.grid()

    # cerrar para evitar conflictos
    plt.close(fig)

    return fig