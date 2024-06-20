import pygame
import sys
import random

# Iniciar Pygame
pygame.init()

# Configurar la pantalla
ANCHO, LARGO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, LARGO))
pygame.display.set_caption("Piedra, Papel o Tijeras")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 36)

# Variables del juego
opciones = ["Piedra", "Papel", "Tijeras"]
opcion_jugador = None
opcion_compu = None
resultado = None

# clase Boton
class Boton:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color

    def draw(self):
        pygame.draw.rect(pantalla, self.color, self.rect)
        text_surface = font.render(self.text, True, NEGRO)
        text_rect = text_surface.get_rect(center=self.rect.center)
        pantalla.blit(text_surface, text_rect)

    def clickear(self, pos):
        return self.rect.collidepoint(pos)

# Crear botones
botones = [
    Boton(100, 400, 150, 50, "Piedra", GRIS),
    Boton(325, 400, 150, 50, "Papel", GRIS),
    Boton(550, 400, 150, 50, "Tijeras", GRIS),
]

# Loop del Juego
corriendo = True
while corriendo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, button in enumerate(botones):
                if button.clickear(event.pos):
                    opcion_jugador = i
                    opcion_compu = random.randint(0, 2)
                    
                    if opcion_jugador == opcion_compu:
                        resultado = "Empate"
                    elif (
                        (opcion_jugador == 0 and opcion_compu == 2)
                        or (opcion_jugador == 1 and opcion_compu == 0)
                        or (opcion_jugador == 2 and opcion_compu == 1)
                    ):
                        resultado = "Ganaste"
                    else:
                        resultado = "Perdiste"

    # Limpiar la pantalla
    pantalla.fill(BLANCO)

    # Dibujar botones
    for button in botones:
        button.draw()

    # Mostrar resultados
    if opcion_jugador is not None:
        player_text = font.render(f"Tu elección: {opciones[opcion_jugador]}", True, NEGRO)
        computer_text = font.render(f"Elección de la computadora: {opciones[opcion_compu]}", True, NEGRO)
        result_text = font.render(resultado, True, NEGRO)

        pantalla.blit(player_text, (50, 100))
        pantalla.blit(computer_text, (50, 150))
        pantalla.blit(result_text, (50, 200))

    # Actualizar la pantalla
    pygame.display.flip()

# Cerrar el juego
pygame.quit()
sys.exit()