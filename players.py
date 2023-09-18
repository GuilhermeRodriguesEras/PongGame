import pygame
from random import choice

class Jogadores():
    def __init__(self,posx,tela,player):
        self.pontos = 0
        self.posY = 220
        self.posX = posx
        self.tela = tela
        self.player = player
        self.final_font = pygame.font.Font('font/OpenSans.ttf',70)
        self.rect = pygame.Rect(self.posX,self.posY,15,160)

    def draw_Player(self):
        self.rect = pygame.Rect(self.posX,self.posY,15,160)
        pygame.draw.rect(self.tela,(255,255,255),self.rect)

        key = pygame.key.get_pressed()
        if self.player == 1:
            if key[pygame.K_w]:
                if self.posY > 0:
                    self.posY -=10
            if key[pygame.K_s]:
                if self.posY < 440:
                    self.posY +=10

        if self.player == 2:
            if key[pygame.K_UP]:
                if self.posY > 0:
                    self.posY -=10
            if key[pygame.K_DOWN]:
                if self.posY < 440:
                    self.posY +=10
    
    def draw_placar(self):
        img = self.final_font.render(str(self.pontos),True,(255,255,255)) 
        if self.player == 1:
            self.tela.blit(img,(150,70))
        else:
            self.tela.blit(img,(710,70))

class Bolinha():
    def __init__(self, superfice, posInicio):
        self.tela = superfice
        self.posInicio = posInicio
        self.pos = self.posInicio
        self.sorteio = True
        self.wayX = 0
        self.wayY = 0

    def drawBolinha(self, RectPlayer1, RectPlayer2, pontuacao):

        puntuacaoFinal = 7
        speed = 10

        if self.sorteio:
            self.wayX = choice([-1,1])
            self.wayY = choice([-1,1])
            self.sorteio = False

        bola = pygame.Rect(self.pos[0],self.pos[1],20,20)
        pygame.draw.rect(self.tela,(255,255,255),bola)

        def ponto(place,points):
            self.sorteio = True
            self.pos = self.posInicio
            if place == 0:
                return points[0], points[1]+1
            else:
                if points[0]+1 == puntuacaoFinal:                
                    self.Fim = True 
                return points[0]+1, points[1]

        if self.pos[0] == 0 or self.pos[0] == 880:
            return ponto(self.pos[0],pontuacao)
        elif self.pos[1] == 0 or self.pos[1] == 580:
            self.wayY *= -1

        if bola.colliderect(RectPlayer1) or bola.colliderect(RectPlayer2):
            self.wayX *= -1

        self.pos = (self.pos[0]+(speed*self.wayX),self.pos[1]+(speed*self.wayY))

        return pontuacao[0], pontuacao[1]