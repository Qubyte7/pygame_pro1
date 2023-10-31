import pygame
from sys import exit
pygame.init()
pygame.display.set_caption("running")
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
surface_width=100
surface_height=200
test_font = pygame.font.Font('beginner/otherss/font/Pixeltype.ttf',50)

player_surface = pygame.image.load('beginner/otherss/graphics/Player/player_walk_1.png').convert_alpha()
sky_surface=pygame.image.load('beginner/otherss/Sky.png').convert()#convert() trandform our png file into something that is easily used by pygame
ground_surface = pygame.image.load('beginner/otherss/graphics/ground.png').convert()
text_surface=test_font.render('SCORE :0',False,'Black')#the second argument is to smooth the edge of the font
snail_surface=pygame.image.load('beginner/otherss/graphics/snail/snail1.png').convert_alpha()#to see the effect of adding _alpha remove it to see what we are trying yo solve
snail_x=600
player_rect=player_surface.get_rect(midbottom =(80,300))
snail_rect=snail_surface.get_rect(topleft =(snail_x,255))
# test_surface = pygame.Surface((surface_width,surface_height))
# test_surface.fill('Gray')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()#once this exit is called it acts as a break in normal execution it will stop the program from there
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(10,10))
    snail_x-=4
    if(snail_x<-100):
        snail_x=800
    screen.blit(snail_surface,snail_rect)
    screen.blit(player_surface,player_rect)

    pygame.display.update()
    clock.tick(60)#here we are telling pygame that our loop should not run the 60fps