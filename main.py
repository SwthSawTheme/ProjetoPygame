import pygame
from pygame.locals import *
from pygame import QUIT
from sys import exit
import time
import random

pygame.init()

largura = 720
altura = 480

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Menu")
FPS = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial",25,True,False)

def run():

    red_x = largura // 2
    red_y = altura // 2
    pontos = 0

    while True:
        texto = fonte.render(f"Pontos:{pontos}",True,WHITE)
        tela.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        
        keys = pygame.key.get_pressed()

        if keys[K_w]:
            red_y -= 10
        if keys[K_s]:
            red_y += 10
        if keys[K_a]:
            red_x -= 10
        if keys[K_d]:
            red_x += 10
        
        mouse = pygame.mouse.get_pos()
        rect_red = pygame.draw.rect(tela,RED,(red_x,red_y,100,80))
        
        if rect_red.collidepoint(mouse):
            tela.fill(BLACK)
            rect_red = pygame.draw.rect(tela,WHITE,(red_x,red_y,50,50))
            pontos += 10
        

        tela.blit(texto,(10,15))
        FPS.tick(60)
        pygame.display.flip()
run()