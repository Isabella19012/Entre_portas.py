
import pygame

def transicao(screen, clock):
    fade = pygame.Surface((1000, 500))
    fade.fill((255, 255, 255))

    for alpha in range(0, 255, 15):
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.display.flip()
        clock.tick(60)

    for alpha in range(255, 0, -15):
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.display.flip()
        clock.tick(60)

def perdeud():
    global perdeux, tela
    perdeux = perdeux+1
    tela='perdeu'
pygame.init()

x, y = 1000, 500
screen = pygame.display.set_mode((x, y)) # configura janela do jogo
clock = pygame.time.Clock()
running = True
tela='tela_menu'
perdeux = 0
fonte=pygame.font.Font(None, 80)
fonte_bemvindo = pygame.font.Font(None, 50)
fonte_txt=pygame.font.Font(None, 40)
subtitulo_fonte = pygame.font.Font(None, 23)

subtitulo = subtitulo_fonte.render(f'As escolham importam', True, 'White')
surface_texto = fonte_bemvindo.render(f"Entre Portas", True, 'White')

voltar = fonte_txt.render(f'<-', True, 'black')
voltar_rect = voltar.get_rect()
voltar_rect.topleft = (30, 55)

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
fundo_instrucao = pygame.image.load("png/ins.png")
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

fundo_fase3 = pygame.image.load('fase3/fundo_fase3.png')
fundo_fase3 = pygame.transform.scale(fundo_fase3, (x, y))
fundo_fase3 = fundo_fase3.convert_alpha

#dicas:
dica_gato = pygame.image.load('png/gatinha.png')
dica_gato = pygame.transform.scale(dica_gato, (150,110))
dicag_rect = dica_gato.get_rect()
dicag_rect.topleft = (557, 110)

mostrar_dica = False
dicatxt = subtitulo_fonte.render("O que mais tem no céu?", True,(255,255,255))
dicatxt_rect = dicatxt.get_rect()
dicatxt_rect.topleft = (120, 90)

#fase 2
#colisão/dica

portaceleiro = pygame.image.load("png/portadoceleiro.png")
portaceleiro = pygame.transform.scale(portaceleiro, (85, 90))
portac_rect = portaceleiro.get_rect()
portac_rect.topleft = (330, 295)

portacasa = pygame.image.load("png/porta_casa.png")
portacasa = pygame.transform.scale(portacasa, (65, 115))
portacasa_rect = portacasa.get_rect()
portacasa_rect.topleft = (830, 320)

dentrocasa = pygame.image.load("png/dentrocasa.png")
dentrocasa = pygame.transform.scale(dentrocasa, (x, y))

portatalvez = pygame.image.load("png/portatalvez.png")
portatalvez = pygame.transform.scale(portatalvez, (68, 185))
portatalvez_rect = portatalvez.get_rect()
portatalvez_rect.topleft = (485, 180)

dicasino = pygame.image.load("png/sino.png")
dicasino = pygame.transform.scale(dicasino, (25, 25))
dicasino_rect = dicasino.get_rect()
dicasino_rect.topleft = (364, 245)

mostrar_dica2 = False
dicatxt2 = subtitulo_fonte.render("Quando tudo termina, pra onde você mais quer ir?",True,(255, 255, 255))
dicatxt2_rect = dicatxt2.get_rect(center=(500, 50))

#fase3
fundo_fase3 = pygame.image.load('fase3/fundo_fase3.png')
fundo_fase3 = pygame.transform.scale(fundo_fase3, (x, y))

dicaredef3 = pygame.image.load('fase3/rededica.png')
dicaredef3 = pygame.transform.scale(dicaredef3, (150, 130))
dica_rede_rect = dicaredef3.get_rect()
dica_rede_rect.topleft = (540, 295)

porta3_1 = pygame.image.load('fase3/portacabana3.png')
porta3_1 = pygame.transform.scale(porta3_1, (52, 65))
porta3_1_rect = porta3_1.get_rect()
porta3_1_rect.topleft = (90, 412)

porta3_2 = pygame.image.load('fase3/portacabana3.png')
porta3_2 = pygame.transform.scale(porta3_2,(52, 65))
porta3_2_rect = porta3_2.get_rect()
porta3_2_rect.topleft = (340, 402)

porta3_3 = pygame.image.load('fase3/portacabana3.png')
porta3_3 = pygame.transform.scale(porta3_3,(52, 65))
porta3_3_rect = porta3_3.get_rect()
porta3_3_rect.topleft = (810, 395)

dentrocabana = pygame.image.load('fase3/fase3_2.png')
dentrocabana = pygame.transform.scale(dentrocabana, (x, y))

dicavela = pygame.image.load('fase3/tocha.png')
dicavela = pygame.transform.scale(dicavela,(40,110))
dicavela_rect = dicavela.get_rect()
dicavela_rect.topleft = (285, 175)

dicavela2 = pygame.image.load('fase3/tocha.png')
dicavela2 = pygame.transform.scale(dicavela2,(40,110))
dicavela2_rect = dicavela2.get_rect()
dicavela2_rect.topleft = (675, 180)

portaverde = pygame.image.load('fase3/portaverde.png')
portaverde = pygame.transform.scale(portaverde,(107,165))
portaverde_rect = portaverde.get_rect()
portaverde_rect.topleft = (535, 235)

prafora = pygame.image.load('fase3/pra fora.png')
prafora = pygame.transform.scale(prafora,( 100,165))
prafora_rect = prafora.get_rect()
prafora_rect.topleft = (377, 235)

mostrar_dica3 = False
dicatxt3 = subtitulo_fonte.render("O que tartaruga, plantas, algas e abacate tem em comum?",True,(255, 255, 255))
dicatxt3_rect = dicatxt3.get_rect(center=(500, 80))

mostrar_dica3_rede = False
dicatxt3_rede = subtitulo_fonte.render("Embaixo da pequena nuvem",True,(255, 255, 255))
dicatxt3_rede_rect = dicatxt3_rede.get_rect(center=(500, 100))

#fase4
fundo_fase4 = pygame.image.load('fase4/fundo_fase4.png')
fundo_fase4 = pygame.transform.scale(fundo_fase4, (x,y))

c1, c2 = 400, 700

carro1 = pygame.image.load('fase4/carroroxo.png')
carro1 = pygame.transform.scale(carro1, (200,100))

carro2 = pygame.image.load('fase4/carroverde.png')
carro2 = pygame.transform.scale(carro2, (200,100))
g1, g1_2 = 80, 40
gatinhodormindo = pygame.image.load('fase4/gatodormindo.png')
gatinhodormindo = pygame.transform.scale(gatinhodormindo, (80,50))
gatinhodormindo_rect = gatinhodormindo.get_rect()
gatinhodormindo_rect.topleft = (g1,g1_2 )

portapredio = pygame.image.load('fase4/portapredio.png')
portapredio = pygame.transform.scale(portapredio, (115, 70))
portapredio_rect = portapredio.get_rect(topleft = (100, 325))

portapredio2 = pygame.image.load('fase4/portapredio.png')
portapredio2 = pygame.transform.scale(portapredio2, (115, 70))
portapredio2_rect = portapredio2.get_rect(topleft = (402, 325))

portaverde4 = pygame.image.load('fase3/portaverde.png')
portaverde4 = pygame.transform.scale(portaverde4, (90, 90))
portaverde4_rect = portaverde4.get_rect(topleft = (803, 300))

dicatxtgato = subtitulo_fonte.render("Onde o gato estava?",True,(255, 255, 255))
dicatxtgato_rect = dicatxt3_rede.get_rect(center=(525, 60))

ganhou_fundo = pygame.image.load('png/ganhou.png')
ganhou_fundo = pygame.transform.scale(ganhou_fundo, (x,y))

perdasbotao = pygame.image.load('png/n de perdas.png')
perdasbotao_rect =perdasbotao.get_rect(topleft = (250, 170))

recomecarbotao = pygame.image.load('png/recomeçar.png')
recomecarbotao_rect =recomecarbotao.get_rect(topleft = (250, 390))

sairbotao = pygame.image.load('png/sair.png')
sairbotao_rect =sairbotao.get_rect(topleft = (250, 280))

fundo_fase5 = pygame.image.load('fase5/fundo5.png')
fundo_fase5 = pygame. transform.scale(fundo_fase5, (x,y))
fundo_fase5 = fundo_fase5.convert_alpha()
p, p2 = 120, 180
h = 235
porta1 = pygame.image.load('fase5/1.png')
porta1 = pygame.transform.scale(porta1, (p,p2))
porta1_rect = porta1.get_rect(topleft = (70, h))

porta2 = pygame.image.load('fase5/2.png')
porta2 = pygame.transform.scale(porta2, (p,p2))
porta2_rect = porta2.get_rect(topleft = (250, h))

porta3 = pygame.image.load('fase5/3.png')
porta3 = pygame.transform.scale(porta3, (p,p2))
porta3_rect = porta3.get_rect(topleft = (450, h))

porta4 = pygame.image.load('fase5/4.png')
porta4 = pygame.transform.scale(porta4, (p,p2))
porta4_rect = porta4.get_rect(topleft = (650, h))

porta5 = pygame.image.load('fase5/5.png')
porta5 = pygame.transform.scale(porta5, (p,p2))
porta5_rect = porta5.get_rect(topleft = (845, h))

while running:

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if tela == 'tela_menu':
                if texto2_rect.collidepoint(event.pos):
                    transicao(screen, clock)
                    tela = 'fase1'
                elif texto3_rect.collidepoint(event.pos):
                    transicao(screen, clock)
                    tela = 'click_instrucoes'

            elif tela == 'click_instrucoes':
                if voltar_rect.collidepoint(event.pos):
                    transicao(screen, clock)
                    tela = 'tela_menu'

            elif tela == 'fase1':
                if dicag_rect.collidepoint(event.pos):
                    mostrar_dica = not mostrar_dica 

                elif porta_errada_rect.collidepoint(event.pos):
                    mostrar_dica = False 
                    transicao(screen, clock)
                    perdeud()

                elif porta_certa1_rect.collidepoint(event.pos):
                    mostrar_dica = False
                    transicao(screen, clock)
                    tela = 'fase2'
                elif voltar_rect.collidepoint(event.pos):
                    transicao(screen, clock)
                    mostrar_dica = False 
                    tela = 'tela_menu'

            elif tela == 'perdeu':
                if botao_voltar_rect.collidepoint(event.pos):
                    transicao(screen, clock)
                    tela = 'tela_menu'
                elif botao_fase1_rect.collidepoint(event.pos):
                    transicao(screen, clock)
                    tela = 'fase1'

            elif tela == 'fase2':
                if voltar_rect.collidepoint(event.pos):
                    mostrar_dica2 = False
                    transicao(screen, clock)
                    tela = 'tela_menu'
                elif portac_rect.collidepoint(event.pos):
                    mostrar_dica2 = False
                    transicao(screen, clock)
                    perdeud()
                elif portacasa_rect.collidepoint(event.pos):
                    mostrar_dica2 = False
                    transicao(screen, clock)
                    tela = 'dentrocasa'
                elif dicasino_rect.collidepoint(event.pos):
                    mostrar_dica2 = not mostrar_dica2
            elif tela == 'dentrocasa': 
                if portatalvez_rect.collidepoint(event.pos):
                    mostrar_dica2 = False
                    transicao(screen, clock)
                    tela = 'fase3'
                elif voltar_rect.collidepoint(event.pos):
                    transicao(screen,clock)
                    tela = 'tela_menu'

            elif tela == 'fase3':
                if voltar_rect.collidepoint(event.pos):
                    mostrar_dica3_rede = False
                    transicao(screen, clock)
                    tela = 'tela_menu'
                elif porta3_1_rect.collidepoint(event.pos):
                    mostrar_dica3_rede = False
                    transicao(screen, clock)
                    perdeud()
                elif porta3_2_rect.collidepoint(event.pos):
                    mostrar_dica3_rede = False
                    transicao(screen, clock)
                    tela = 'dentrocabana'
                elif porta3_3_rect.collidepoint(event.pos):
                    mostrar_dica3_rede = False
                    transicao(screen, clock)
                    perdeud()
                elif dica_rede_rect.collidepoint(event.pos):
                    mostrar_dica3_rede = not mostrar_dica3_rede
            elif tela == 'dentrocabana':
                if dicavela_rect.collidepoint(event.pos) or dicavela2_rect.collidepoint(event.pos):
                    mostrar_dica3 = not mostrar_dica3
                elif voltar_rect.collidepoint(event.pos):
                    mostrar_dica3 = False
                    transicao(screen, clock)
                    tela = 'tela_menu'
                elif prafora_rect.collidepoint(event.pos):
                    mostrar_dica3 = False
                    transicao(screen, clock)
                    perdeud()
                elif portaverde_rect.collidepoint(event.pos):
                    mostrar_dica3 = False
                    transicao(screen, clock)
                    tela = 'fase4'
            elif tela == 'fase4':
                if gatinhodormindo_rect.collidepoint(event.pos):
                    gatinhodormindo = pygame.image.load('fase4/gato acordado.png')
                    gatinhodormindo = pygame.transform.scale(gatinhodormindo, (80,50))
                    gatinhodormindo_rect = gatinhodormindo.get_rect()
                    gatinhodormindo_rect.topleft = (g1,g1_2 )
                    g1=g1+40
                    print(g1)
                    print(g1_2)
                    if g1 == 520:
                        g1_2 = 60
                    elif g1_2 == 60:
                        g1_2 = 70
                    elif g1 == 720:
                        g1_2 = 130
                    elif g1_2 == 130:
                        g1_2 = 175
                elif voltar_rect.collidepoint(event.pos):
                    mostrar_dica_gato4 = False
                    transicao(screen, clock)
                    tela = 'tela_menu'
                elif  portaverde4_rect.collidepoint(event.pos):
                    mostrar_dica_gato4 = False
                    transicao(screen, clock)
                    perdeud()
                elif portapredio_rect.collidepoint(event.pos):
                    mostrar_dica_gato4 = False
                    transicao(screen,clock)
                    tela ='fase5'
                elif portapredio2_rect.collidepoint(event.pos):
                    mostrar_dica_gato4 = False
                    transicao(screen, clock)
                    perdeud()

            elif tela == 'ganhou':
                transicao(screen,clock)
                if sairbotao_rect.collidepoint(event.pos):
                    running = False
                elif recomecarbotao_rect.collidepoint(event.pos):
                    tela ='tela_menu'
            elif tela == 'fase5':
                transicao(screen, clock)
                if porta1_rect.collidepoint(event.pos):
                    perdeud()
                elif porta2_rect.collidepoint(event.pos):
                    perdeud()
                elif porta3_rect.collidepoint(event.pos):
                    perdeud()
                elif porta4_rect.collidepoint(event.pos):
                    tela = 'ganhou'
                elif porta5_rect.collidepoint(event.pos):
                    perdeud()

#TELAS
    if tela == 'tela_menu':
        
        screen.blit(fundo, (0, 0))
        pygame.draw.rect(screen, (226, 81, 0), (0, 0, x, 100))
        pygame.draw.rect(screen, (226, 81, 0), (0, 400, x, 120))
        screen.blit(subtitulo, (405, 70))
        screen.blit(surface_texto, (380, 30))
        pygame.draw.rect(screen, (255, 255, 255), (230, 410, 230, 70), 3, 12)
        pygame.draw.rect(screen, (255, 255, 255), (510, 410, 230, 70), 3, 12)
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
        screen.blit(dica_gato, dicag_rect.topleft)
        screen.blit(porta_errada1, porta_errada_rect)
        screen.blit(porta_certa1, porta_certa1_rect)
        screen.blit(voltar, voltar_rect)
        if mostrar_dica:
            pygame.draw.rect(screen, (255, 255, 255), (90, 80, 250, 40), 3, 12)
            screen.blit(dicatxt, dicatxt_rect)

        if porta_certa1_rect.collidepoint(mouse_pos) or porta_errada_rect.collidepoint(mouse_pos) or voltar_rect.collidepoint(mouse_pos) or dicag_rect.collidepoint(mouse_pos):
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
        screen.blit(portaceleiro, portac_rect)
        screen.blit(portacasa, portacasa_rect)
        screen.blit(dicasino, dicasino_rect)
        if mostrar_dica2:
            pygame.draw.rect(screen, (255, 255, 255), (300, 30, 400, 40), 3, 12)
            screen.blit(dicatxt2, dicatxt2_rect)
        if voltar_rect.collidepoint(mouse_pos) or dicasino_rect.collidepoint(mouse_pos) or portac_rect.collidepoint(mouse_pos) or portacasa_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    elif tela == 'fase3':
        screen.blit(fundo_fase3, (0,0))
        screen.blit(voltar, voltar_rect)
        screen.blit(dicaredef3, dica_rede_rect)
        screen.blit(porta3_1, porta3_1_rect)
        screen.blit(porta3_2, porta3_2_rect)
        screen.blit(porta3_3, porta3_3_rect)
        if mostrar_dica3_rede:
            pygame.draw.rect(screen, (255, 255, 255), (350, 85, 300, 30), 3, 12)
            screen.blit(dicatxt3_rede, dicatxt3_rede_rect)
        if voltar_rect.collidepoint(mouse_pos) or dica_rede_rect.collidepoint(mouse_pos) or porta3_1_rect.collidepoint(mouse_pos) or porta3_2_rect.collidepoint(mouse_pos) or porta3_3_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    elif tela == 'dentrocasa':
        screen.blit(dentrocasa, (0,0))
        screen.blit(voltar, voltar_rect)
        screen.blit(portatalvez, portatalvez_rect)
        if portatalvez_rect.collidepoint(mouse_pos) or voltar_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    elif tela == 'dentrocabana':
        screen.blit(dentrocabana, (0, 0))
        screen.blit(voltar, voltar_rect)
        screen.blit(dicavela, dicavela_rect)
        screen.blit(dicavela2, dicavela2_rect)
        screen.blit(portaverde, portaverde_rect)
        screen.blit(prafora, prafora_rect)
        if mostrar_dica3:
            pygame.draw.rect(screen, (255, 255, 255), (280, 60, 450, 40), 3, 12)
            screen.blit(dicatxt3, dicatxt3_rect)

        if voltar_rect.collidepoint(mouse_pos) or prafora_rect.collidepoint(mouse_pos) or dicavela_rect.collidepoint(mouse_pos) or portaverde_rect.collidepoint(mouse_pos) or dicavela2_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    elif tela == 'fase4':
        c1 = c1+10
        c2 = c2 -10
        screen.blit(fundo_fase4, (0,0))
        screen.blit(voltar, voltar_rect)
        screen.blit(gatinhodormindo, gatinhodormindo_rect)
        screen.blit(carro1, (c1, 380))
        screen.blit(carro2, (c2, 400))
        screen.blit(portaverde4, portaverde4_rect)
        screen.blit(portapredio, portapredio_rect)
        screen.blit(portapredio2, portapredio2_rect)
        if g1>=1040:
            pygame.draw.rect(screen, (255, 255, 255), (400, 40, 190, 40), 3, 12)
            screen.blit(dicatxtgato, dicatxtgato_rect)
        if voltar_rect.collidepoint(mouse_pos) or portaverde4_rect.collidepoint(mouse_pos) or portapredio2_rect.collidepoint(mouse_pos)or portapredio_rect.collidepoint(mouse_pos) or  gatinhodormindo_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    elif tela == 'fase5':
        screen.blit(fundo_fase5, (0,0))
        screen.blit(porta1, porta1_rect)
        screen.blit(porta2, porta2_rect)
        screen.blit(porta3, porta3_rect)
        screen.blit(porta4, porta4_rect)
        screen.blit(porta5, porta5_rect)

        if porta1_rect.collidepoint(mouse_pos) or porta2_rect.collidepoint(mouse_pos) or porta3_rect.collidepoint(mouse_pos) or porta4_rect.collidepoint(mouse_pos) or porta5_rect.collidepoint(mouse_pos):
             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)           
    elif tela == 'ganhou':
        perdeuXvezes = fonte_bemvindo.render(f'{perdeux}', True, 'Yellow')
        screen.blit(ganhou_fundo, (0,0))
        screen.blit(perdasbotao, perdasbotao_rect)
        screen.blit(sairbotao, sairbotao_rect)
        screen.blit(recomecarbotao, recomecarbotao_rect)
        screen.blit(perdeuXvezes, (600, 210))
        if recomecarbotao_rect.collidepoint(mouse_pos) or sairbotao_rect.collidepoint(mouse_pos) or perdasbotao_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)           


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
