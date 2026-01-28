import pygame

pygame.init()
x, y = 1000, 500
screen = pygame.display.set_mode((x, y)) # configura janela do jogo
clock = pygame.time.Clock()
running = True
tela='tela_menu'

fonte=pygame.font.Font(None, 80)
fonte_bemvindo = pygame.font.Font(None, 50)
fonte_txt=pygame.font.Font(None, 40)
subtitulo_fonte = pygame.font.Font(None, 23)

subtitulo = subtitulo_fonte.render(f'As escolham importam', True, 'White')
surface_texto = fonte_bemvindo.render(f"Entre Portas", True, 'White')

voltar = fonte_txt.render(f'<-', True, (192, 79, 21))
voltar_rect = voltar.get_rect()
voltar_rect.topleft = (10, 55)

#jogar e instruções
texto2 = fonte_txt.render(f'Jogar <-', True, 'White')
texto2_rect = texto2.get_rect()
texto2_rect.topleft = (295, 435)

texto3 = fonte_txt.render(f'Instruções <-', True, 'White')
texto3_rect = texto3.get_rect()
texto3_rect.topleft = (535, 435)

#fundo do inicio
fundo = pygame.image.load("jpg/fundo_por do sol.jpg")
fundo = pygame.transform.scale(fundo, (x, y)) 
#fundo do perdeu
perdeu = pygame.image.load('png/voceperdeu.png')
perdeu = pygame.transform.scale(perdeu, (x, y)) 
#fundo instrução
fundo_instrucao = pygame.image.load("png/fundo instrução2.png")
fundo_instrucao = pygame.transform.scale(fundo_instrucao, (x, y))
fundo_instrucao = fundo_instrucao.convert_alpha()
#porta errada e certa
porta_certa1 = pygame.image.load('png/porta_primeira fase_estrela.png')
porta_certa1 = pygame.transform.scale(porta_certa1, (75, 130))
porta_certa1_rect = porta_certa1.get_rect()
porta_certa1_rect.topleft = (10, 270)

porta_errada1 = pygame.image.load('jpg/porta_da_primeira_fase.jpg')
porta_errada1 = pygame.transform.scale(porta_errada1, (75, 130))
porta_errada_rect = porta_errada1.get_rect()
porta_errada_rect.topleft = (905, 270)
#perdeu, fase 1 e novamente.
botao_fase1 = pygame.image.load('png/voltar_fase1.png')
botao_fase1_rect = botao_fase1.get_rect()
botao_fase1_rect.topleft = (100, 300)

botao_voltar = pygame.image.load('png/voltar_menu.png')
botao_voltar_rect = botao_voltar.get_rect()
botao_voltar_rect.topleft = (550, 300)

# fundo das fases
fundo_fase1 = pygame.image.load('png/fundo_fase1.png')
fundo_fase1 = pygame.transform.scale(fundo_fase1, (x, y))
fundo_fase1 = fundo_fase1.convert_alpha()

fundo_fase2 = pygame.image.load('png/cenario_fase2.png')
fundo_fase2 = pygame.transform.scale(fundo_fase2, (x, y))
fundo_fase2 = fundo_fase2.convert_alpha()
#desistir
desistir = fonte_txt.render(f'Menu <-', True, 'White')
desistir_rect = desistir.get_rect()
desistir_rect.topleft = (850,30)


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
        elif porta_errada_rect.collidepoint(event.pos):
          tela = 'perdeu'
        elif botao_fase1_rect.collidepoint(event.pos):
           tela = 'fase1'
        elif botao_voltar_rect.collidepoint(event.pos):
           tela = 'tela_menu'
        elif desistir_rect.collidepoint(event.pos):
          tela = "tela_menu"
        elif porta_certa1_rect.collidepoint(event.pos):
          tela = 'fase2'

           
    if tela == 'tela_menu':

      screen.blit(fundo, (0, 0)) #0,0, 153 - tela fase 1
      pygame.draw.rect(screen, (226, 81, 0), (0, 0, x, 100))
      pygame.draw.rect(screen, (226, 81, 0), (0, 400, x, 120))
      #subtitulo
      screen.blit(subtitulo, (405, 70))
      screen.blit(surface_texto, (380, 30))  
      #bordas do >botao<
      pygame.draw.rect(screen, (255, 255, 255), (230, 410, 230, 70), (border_radius:=5))
      pygame.draw.rect(screen, (255, 255, 255), (510, 410, 230, 70), (border_radius:=5))

      screen.blit(texto2, texto2_rect.topleft)  
      screen.blit(texto3, texto3_rect.topleft) 

    if tela == "click_jogar":
        tela = 'fase1'
    elif tela == "click_instrucoes":
        
      screen.blit(fundo_instrucao, (0,0))
      screen.blit(voltar, voltar_rect.topleft)

    if tela == 'fase1':
      screen.blit(fundo_fase1,  (0,0))
      screen.blit(porta_errada1, porta_errada_rect.topleft)
      screen.blit(porta_certa1, porta_certa1_rect)
      screen.blit(desistir, desistir_rect.topleft)
    if tela == 'perdeu':
      screen.blit(perdeu, (0, 0))
      screen.blit(botao_voltar, botao_voltar_rect.topleft)
      screen.blit(botao_fase1, botao_fase1_rect.topleft)
    if tela == 'fase2':
      screen.blit(fundo_fase2, (0,0))
      screen.blit(voltar, voltar_rect.topleft)
        
    pygame.display.flip() 
    clock.tick(60)  

pygame.quit()
