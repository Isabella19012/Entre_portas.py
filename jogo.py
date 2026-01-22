import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500)) # configura janela do jogo
clock = pygame.time.Clock()
running = True

fonte=pygame.font.Font(None, 50)
fonte_txt=pygame.font.Font(None, 28)

surface_texto = fonte.render(f"Bem vindo!", True, 'White')

texto2 = fonte_txt.render(f'Jogar', True, 'White')
texto2_rect = texto2.get_rect()
texto2_rect.topleft = (20, 150)

texto3 = fonte_txt.render(f'Instruções', True, 'White')
texto3_rect = texto3.get_rect()
texto3_rect.topleft = (20, 200)

while running:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
    # Check if the left button was clicked (button 1)
       if event.button == 1:
       # Check for collision between mouse position and the object's Rect
        if texto2_rect.collidepoint(event.pos):
          print('A')
        elif texto3_rect.collidepoint(event.pos):
          print("a")
            

    screen.fill((0, 0, 0)) #0,0, 153 - tela fase 1
    screen.blit(surface_texto, (20, 100))  
    screen.blit(texto2, texto2_rect.topleft)  
    screen.blit(texto3, texto3_rect.topleft) 
    pygame.display.flip() 
    
    clock.tick(60)  

pygame.quit()
