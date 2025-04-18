import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.font.init()

# Window setup
display = pygame.display.set_mode((400, 600))
pygame.display.set_caption('TECALDOOOUUUBS')
bg = pygame.image.load("pipi.png")
white = (255, 255, 255)

# Load all sounds once
sounds = {
    K_q: pygame.mixer.Sound('C.wav'),
    K_w: pygame.mixer.Sound('C#.wav'),
    K_e: pygame.mixer.Sound('D.wav'),
    K_r: pygame.mixer.Sound('D#.wav'),
    K_t: pygame.mixer.Sound('E.wav'),
    K_y: pygame.mixer.Sound('F.wav'),
    K_u: pygame.mixer.Sound('F#.wav'),
    K_i: pygame.mixer.Sound('G.wav'),
    K_o: pygame.mixer.Sound('G#.wav'),
    K_p: pygame.mixer.Sound('A.wav'),
    K_a: pygame.mixer.Sound('A#.wav'),
    K_s: pygame.mixer.Sound('B.wav'),
    K_d: pygame.mixer.Sound('Cmin.wav'),
    K_f: pygame.mixer.Sound('Cmin#.wav'),
    K_g: pygame.mixer.Sound('Dmin.wav'),
    K_h: pygame.mixer.Sound('Dmin#.wav'),
    K_j: pygame.mixer.Sound('Emin.wav'),
}

# Set volume for all sounds
for sound in sounds.values():
    sound.set_volume(0.4)

# Setup enough channels
pygame.mixer.set_num_channels(32)
channel_index = 0

while True:
    display.fill(white)
    display.blit(bg, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key in sounds:
                pygame.mixer.Channel(channel_index).play(sounds[event.key])
                channel_index = (channel_index + 1) % 32  # cycle through channels

            if event.key == pygame.K_x:
                pygame.quit()
                sys.exit()
