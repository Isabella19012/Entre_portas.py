import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500)) # configura janela do jogo
clock = pygame.time.Clock()
running = True
tela='tela_menu'

fonte=pygame.font.Font(None, 80)
fonte_bemvindo = pygame.font.Font(None, 50)
fonte_txt=pygame.font.Font(None, 28)
subtitulo_fonte = pygame.font.Font(None, 23)

subtitulo = subtitulo_fonte.render(f'As escolham importam', True, 'White')

surface_texto = fonte_bemvindo.render(f"Entre Portas", True, 'White')

voltar = fonte.render(f'Voltar', True, "Purple")
voltar_rect = voltar.get_rect()
voltar_rect.topleft = (10, 50)

#instrucao = fonte.render(f'Instrução', True, (192, 79, 21))
#instrucao_rect = instrucao.get_rect()
#instrucao_rect.topleft = (330, 50)

texto2 = fonte_txt.render(f'Jogar <-', True, 'White')
texto2_rect = texto2.get_rect()
texto2_rect.topleft = (20, 150)

texto3 = fonte_txt.render(f'Instruções <-', True, 'White')
texto3_rect = texto3.get_rect()
texto3_rect.topleft = (20, 200)

fundo = pygame.image.load("fundo_por do sol.jpg")
fundo = pygame.transform.scale(fundo, (800, 500)) 

fundo_instrucao = pygame.image.load("Design sem nome.png")

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

        #elif fase1_rect.collidepoint(event.pos):
         #  tela ='fase1'
        #elif fase2_rect.collidepoint(event.pos):
          # tela ='fase1'
        #elif fase3_rect.collidepoint(event.pos):
          # tela ='fase5'
        #elif fase4_rect.collidepoint(event.pos):
          # tela = 'fase4'
        #elif fase5_rect.collidepoint(event.pos):
          # tela = 'fase5'
        #elif voceperdeu_rect.collidepoint(event.pos):
          # tela = 'voceperdeu'
           
    if tela == 'tela_menu':

      screen.blit(fundo, (0, 0)) #0,0, 153 - tela fase 1
      pygame.draw.rect(screen, (226, 81, 0), (0, 0, 800, 100))
      pygame.draw.rect(screen, (226, 81, 0), (0, 400, 800, 120))
      screen.blit(subtitulo, (300, 70))
      screen.blit(surface_texto, (275, 30))  
      screen.blit(texto2, texto2_rect.topleft)  
      screen.blit(texto3, texto3_rect.topleft) 

    if tela == "click_jogar":
        screen.fill((0, 0, 153))
        #screen.blit(fase1, fase1_rect.center)
        print('nada ainda')
    elif tela == "click_instrucoes":
        
        screen.blit(fundo_instrucao, (0,0))
        screen.blit(voltar, voltar_rect.topleft)
    #    screen.blit(instrucao, instrucao_rect.topleft)
        
    pygame.display.flip() 
    clock.tick(60)  

pygame.quit()
