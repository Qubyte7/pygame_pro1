import pygame
from sys import exit
pygame.init()
pygame.display.set_caption("running")
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()#once this exit is called it acts as a break in normal execution it will stop the program from there
    pygame.display.update()
    clock.tick(60)#here we are telling pygame that our loop should not run the 60fps