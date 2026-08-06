import sys

try:
    import torch
    import torch.nn as nn
except ImportError:
    print("[ERROR] La librería 'torch' no está instalada.")
    print("Ejecuta en tu terminal: pip install torch torchvision")
    sys.exit(1)


def demo_pytorch():
    # 1. Comprobar aceleración por GPU (CUDA / ROCm / DirectML)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"\n--- Dispositivo de Cómputo Seleccionado: {device} ---")

    # 2. Creación de Tensores con seguimiento de gradiente habilitado
    # Creamos un tensor de entrada X y unos pesos W
    X = torch.tensor([[1.0, 2.0], [3.0, 4.0]], device=device)
    W = torch.tensor([[0.5], [1.5]], requires_grad=True, device=device)

    print("\nTensor de Entrada (X):")
    print(X)
    print("\nTensor de Pesos (W) [con requires_grad=True]:")
    print(W)

    # 3. Paso Hacia Adelante (Forward Pass): Multiplicación matricial
    Y_pred = torch.matmul(X, W)
    print("\nResultado de Inferencia (Y_pred = X @ W):")
    print(Y_pred)

    # 4. Cálculo de Función de Pérdida (Loss) y Retropropagación (Backpropagation)
    Y_target = torch.tensor([[3.0], [7.0]], device=device)
    loss_fn = nn.MSELoss()
    loss = loss_fn(Y_pred, Y_target)

    print(f"\nPérdida calculada (MSE Loss): {loss.item():.4f}")

    # Ejecutar la diferenciación automática para obtener gradientes
    loss.backward()

    print("\nGradiente calculado para los pesos (W.grad):")
    print(W.grad)


if __name__ == "__main__":
    demo_pytorch()