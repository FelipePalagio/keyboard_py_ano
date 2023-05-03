import pygame, sys
from pygame.locals import *

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 12)



display = pygame.display.set_mode((400, 600))
pygame.display.set_caption('TECALDOOOUUUBS')
bg = pygame.image.load("pipi.png")
white = (255, 255, 255)
black = (0, 0, 0)

while True:
 
    display.fill((white))
    display.blit(bg, (0, 0))



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:

                C = pygame.mixer.Sound('C.wav')
                C.set_volume(0.4)
                pygame.mixer.Channel(0).play(C)

            if event.key == pygame.K_w:

                Csharp = pygame.mixer.Sound('C#.wav')
                Csharp.set_volume(0.4)
                pygame.mixer.Channel(1).play(Csharp)



            if event.key == pygame.K_e:

                D = pygame.mixer.Sound('D.wav')
                D.set_volume(0.4)
                pygame.mixer.Channel(2).play(D)

            if event.key == pygame.K_r:

                Dsharp = pygame.mixer.Sound('D#.wav')
                Dsharp.set_volume(0.4)
                pygame.mixer.Channel(3).play(Dsharp)

            if event.key == pygame.K_t:

                E = pygame.mixer.Sound('E.wav')
                E.set_volume(0.4)
                pygame.mixer.Channel(4).play(E)

            if event.key == pygame.K_y:

                F = pygame.mixer.Sound('F.wav')
                F.set_volume(0.4)
                pygame.mixer.Channel(5).play(F)

            if event.key == pygame.K_u:

                Fsharp = pygame.mixer.Sound('F#.wav')
                Fsharp.set_volume(0.4)
                pygame.mixer.Channel(6).play(Fsharp)

            if event.key == pygame.K_i:

                G = pygame.mixer.Sound('G.wav')
                G.set_volume(0.4)
                pygame.mixer.Channel(7).play(G)

            if event.key == pygame.K_o:

                Gsharp = pygame.mixer.Sound('G#.wav')
                Gsharp.set_volume(0.4)
                pygame.mixer.Channel(0).play(Gsharp)

            if event.key == pygame.K_p:

                A = pygame.mixer.Sound('A.wav')
                A.set_volume(0.4)
                pygame.mixer.Channel(1).play(A)

            if event.key == pygame.K_a:

                Asharp = pygame.mixer.Sound('A#.wav')
                Asharp.set_volume(0.4)
                pygame.mixer.Channel(2).play(Asharp)

            if event.key == pygame.K_s:

                B = pygame.mixer.Sound('B.wav')
                B.set_volume(0.4)
                pygame.mixer.Channel(3).play(B)

            if event.key == pygame.K_d:

                Cmin = pygame.mixer.Sound('Cmin.wav')
                Cmin.set_volume(0.4)
                pygame.mixer.Channel(3).play(Cmin)

            if event.key == pygame.K_f:

                Cminsharp = pygame.mixer.Sound('Cmin#.wav')
                Cminsharp.set_volume(0.4)
                pygame.mixer.Channel(3).play(Cminsharp)

            if event.key == pygame.K_g:

                Dmin = pygame.mixer.Sound('Dmin.wav')
                Dmin.set_volume(0.4)
                pygame.mixer.Channel(3).play(Dmin)

            if event.key == pygame.K_h:

                Dminsharp = pygame.mixer.Sound('Dmin#.wav')
                Dminsharp.set_volume(0.4)
                pygame.mixer.Channel(3).play(Dminsharp)

            if event.key == pygame.K_j:

                Emin = pygame.mixer.Sound('Emin.wav')
                Emin.set_volume(0.4)
                pygame.mixer.Channel(3).play(Emin)

            if event.key == pygame.K_x:
                sys.exit()



