import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500)) # configura janela do jogo
clock = pygame.time.Clock()
running = True
tela='tela_menu'

fonte=pygame.font.Font(None, 50)
fonte_txt=pygame.font.Font(None, 28)

surface_texto = fonte.render(f"Bem vindo!", True, 'White')

voltar = fonte.render(f'Voltar', True, "Purple")
voltar_rect = voltar.get_rect()
voltar_rect.topleft = (10, 50)

instrucao = fonte.render(f'Instrução', True, "Black")
instrucao_rect = instrucao.get_rect()
instrucao_rect.topleft = (330, 50)

texto2 = fonte_txt.render(f'Jogar <-', True, 'White')
texto2_rect = texto2.get_rect()
texto2_rect.topleft = (20, 150)

texto3 = fonte_txt.render(f'Instruções <-', True, 'White')
texto3_rect = texto3.get_rect()
texto3_rect.topleft = (20, 200)

fundo = pygame.image.load("fundo_da_abertura.jpg")
fundo = pygame.transform.scale(fundo, (800, 500)) 

fundo_instrucao = pygame.image.load("fundo_ instrucao.jpg")
fundo_instrucao = pygame.transform.scale(fundo_instrucao, (800, 500))

while running:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
    # Check if the left button was clicked (button 1)
       if event.button == 1:
       # Check for collision between mouse position and the object's Rect
        if texto2_rect.collidepoint(event.pos):
          tela = "click_jogar"
        elif texto3_rect.collidepoint(event.pos):
          tela =  'click_instrucoes'
        elif voltar_rect.collidepoint(event.pos):
           tela = "tela_menu"
            

    if tela == 'tela_menu':
      screen.blit(fundo, (0, 0)) #0,0, 153 - tela fase 1
      screen.blit(surface_texto, (20, 90))  
      screen.blit(texto2, texto2_rect.topleft)  
      screen.blit(texto3, texto3_rect.topleft) 


    if tela == "click_jogar":
        screen.fill((0, 0, 153))
        print('nada ainda')
    elif tela == "click_instrucoes":
        
        screen.blit(fundo_instrucao, (0,0))
        screen.blit(voltar, voltar_rect.topleft)
        screen.blit(instrucao, instrucao_rect.topleft)
        
    pygame.display.flip() 
    clock.tick(60)  

pygame.quit()
