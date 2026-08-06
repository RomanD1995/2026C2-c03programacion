import sys

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("[ERROR] La librería 'matplotlib' no está instalada.")
    print("Ejecuta en tu terminal: pip install matplotlib")
    sys.exit(1)


def demo_matplotlib():
    # 1. Datos simulados de entrenamiento (Épocas vs. Pérdida)
    epocas = list(range(1, 11))
    pérdida_entrenamiento = [0.95, 0.70, 0.52, 0.38, 0.29, 0.22, 0.18, 0.15, 0.12, 0.10]
    pérdida_validación = [0.98, 0.75, 0.58, 0.44, 0.36, 0.31, 0.29, 0.28, 0.27, 0.70]

    # 2. Crear la figura y los ejes del gráfico
    plt.figure(figsize=(8, 5))

    # 3. Graficar las líneas de entrenamiento y validación
    plt.plot(epocas, pérdida_entrenamiento, label="Pérdida Entrenamiento", marker="o", color="blue")
    plt.plot(epocas, pérdida_validación, label="Pérdida Validación", marker="s", color="red", linestyle="--")

    # 4. Personalizar el gráfico (Título, Etiquetas, Rejilla y Leyenda)
    plt.title("Monitoreo de Pérdida (Loss) durante el Entrenamiento", fontsize=14)
    plt.xlabel("Épocas", fontsize=12)
    plt.ylabel("Pérdida (MSE Loss)", fontsize=12)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()

    # 5. Guardar la figura generada en el disco
    nombre_archivo = "curva_entrenamiento.png"
    plt.savefig(nombre_archivo, dpi=300, bbox_inches="tight")
    print(f"\n[ÉXITO] Gráfico generado y guardado exitosamente como '{nombre_archivo}'.")

    # 6. Mostrar el gráfico en pantalla
    plt.show()


if __name__ == "__main__":
    demo_matplotlib()