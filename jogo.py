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
#dicas:
dica_gato = pygame.image.load('png/gatinha.png')
dicag_rect = dica_gato.get_rect

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if tela == 'tela_menu':
                if texto2_rect.collidepoint(event.pos):
                    tela = 'fase1'
                elif texto3_rect.collidepoint(event.pos):
                    tela = 'click_instrucoes'

            elif tela == 'click_instrucoes':
                if voltar_rect.collidepoint(event.pos):
                    tela = 'tela_menu'

            elif tela == 'fase1':
                if porta_errada_rect.collidepoint(event.pos):
                    tela = 'perdeu'
                elif porta_certa1_rect.collidepoint(event.pos):
                    tela = 'fase2'
                elif desistir_rect.collidepoint(event.pos):
                    tela = 'tela_menu'

            elif tela == 'perdeu':
                if botao_voltar_rect.collidepoint(event.pos):
                    tela = 'tela_menu'
                elif botao_fase1_rect.collidepoint(event.pos):
                    tela = 'fase1'

            elif tela == 'fase2':
                if voltar_rect.collidepoint(event.pos):
                    tela = 'tela_menu'

    mouse_pos = pygame.mouse.get_pos()

#TELAS
    if tela == 'tela_menu':
        screen.blit(fundo, (0, 0))
        pygame.draw.rect(screen, (226, 81, 0), (0, 0, x, 100))
        pygame.draw.rect(screen, (226, 81, 0), (0, 400, x, 120))
        screen.blit(subtitulo, (405, 70))
        screen.blit(surface_texto, (380, 30))
        pygame.draw.rect(screen, (255, 255, 255), (230, 410, 230, 70), 2, 5)
        pygame.draw.rect(screen, (255, 255, 255), (510, 410, 230, 70), 2, 5)
        screen.blit(texto2, texto2_rect)
        screen.blit(texto3, texto3_rect)

        if texto2_rect.collidepoint(mouse_pos) or texto3_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


    elif tela == 'click_instrucoes':
        screen.blit(fundo_instrucao, (0, 0))
        screen.blit(voltar, voltar_rect)
        
        if voltar_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    

    elif tela == 'fase1':
        screen.blit(fundo_fase1, (0, 0))
        screen.blit(porta_errada1, porta_errada_rect)
        screen.blit(porta_certa1, porta_certa1_rect)
        screen.blit(desistir, desistir_rect)

        if porta_certa1_rect.collidepoint(mouse_pos) or porta_errada_rect.collidepoint(mouse_pos) or desistir_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


    elif tela == 'perdeu':
        screen.blit(perdeu, (0, 0))
        screen.blit(botao_voltar, botao_voltar_rect)
        screen.blit(botao_fase1, botao_fase1_rect)
        if botao_voltar_rect.collidepoint(mouse_pos) or botao_fase1_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    elif tela == 'fase2':
        screen.blit(fundo_fase2, (0, 0))
        screen.blit(voltar, voltar_rect)

        if voltar_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
