import pygame as pg
import sys
from pathlib import Path

ROOTH_PATH = Path(__file__).parent
pg.init()

# Configuração de tela:
WIDHT = 800
HEIGHT = 600
WINDOW_SIZE = (WIDHT, HEIGHT)
window = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("BOTÃO DE EMERGÊNCIA!")


# CORES:

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
IMAGE = pg.image.load(ROOTH_PATH / "shiba_meme.png")

# POSIÇÂO DA IMAGEM:

IMAGE_RECT = IMAGE.get_rect()
IMAGE_RECT_CENTER = (WIDHT // 2, HEIGHT //2) 
# Propriedades do balão:

BALLOON_RADIUS = 50
BALLOON_COLOR = RED
BALLOON_POSITION = (WIDHT // 2, HEIGHT // 2)

def draw_balloon():
    pg.draw.circle(window, BALLOON_COLOR, BALLOON_POSITION, BALLOON_RADIUS)

def clicado(mouse_pos):
    distance_squared = (mouse_pos[0] - BALLOON_POSITION[0]) ** 2 + (mouse_pos[1] - BALLOON_POSITION[1])**2
    return distance_squared <= BALLOON_RADIUS**2

while True:
    window.fill(WHITE)
    window.blit(IMAGE, IMAGE_RECT)
    
    draw_balloon()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pg.mouse.get_pos()
                if clicado(mouse_pos):
                    print("SISTEMA SENDO DESLIGADO....")
                    
    pg.display.flip()