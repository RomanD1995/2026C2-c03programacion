import pygame

# Inicializar los módulos de Pygame
pygame.init()

# Definir las dimensiones de la ventana
ancho = 600
alto = 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Ejemplo de Ventana Interactiva - Pygame")

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        # Detectar el evento de cerrar la ventana
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Actualizar la pantalla
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()