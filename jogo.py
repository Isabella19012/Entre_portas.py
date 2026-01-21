import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500)) # configura janela do jogo
clock = pygame.time.Clock()
running = True

fonte=pygame.font.Font(None, 50)
fonte_txt2=pygame.font.Font(None, 32)
fonte_txt3=pygame.font.Font(None, 30)

surface_texto = fonte.render(f"Bem vindo!", True, 'White')
texto2 = fonte_txt2.render(f'Dica 1: Use o mouse para abrir uma porta e passar de fase', True, 'White')
texto3 = fonte_txt3.render(f'Dica 2: Também pode usar o mouse para clicar em itens que te darão mais dicas', True, 'White')

while running:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

    screen.fill((0, 0, 150)) #0,0, 153 - tela fase 1
    screen.blit(surface_texto, (300, 100))  
    screen.blit(texto2, ( 20, 150))  
    screen.blit(texto3, ( 20, 200)) 
    pygame.display.flip() 

    clock.tick(60)  

pygame.quit()
