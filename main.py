import pygame
from players import Jogadores, Bolinha

pygame.init()

screen_width, screen_height = 900, 600

clock = pygame.time.Clock()
FPS = 60

white = (255,255,255)

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Projeto IA")

player1 = Jogadores(20,screen,1)
player2 = Jogadores(865,screen,2)
bolinha = Bolinha(screen,(440,290))

run = True
while run:
    clock.tick(FPS)

    screen.fill((0,0,0))

    pygame.draw.rect(screen,(255,255,255),(screen_width//2,0,2,600))

    player1.draw_Player()
    player2.draw_Player()

    player1.draw_placar()
    player2.draw_placar()

    player1.pontos, player2.pontos = bolinha.drawBolinha(player1.rect, player2.rect, (player1.pontos,player2.pontos))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

