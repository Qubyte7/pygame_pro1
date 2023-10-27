import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH=600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))

player = pygame.Rect((300,250,50,50))



trying=True

while trying:
   screen.fill((0,0,0))
   pygame.draw.rect(screen,(255,255,255),player)
   
   key =pygame.key.get_pressed()
   if key[pygame.K_a]==True:
       player.move_ip(-1,0)
   elif key[pygame.K_d]==True:
       player.move_ip(1,0)
   elif key[pygame.K_w]==True:
       player.move_ip(0,-1)
   elif key[pygame.K_s]==True:
       player.move_ip(0,1) 
   elif key[pygame.K_a] and key[pygame.K_w] ==True:
       player.move_ip(-1,-1)

   pygame.display.update()
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
            trying=False

pygame.quit()      

