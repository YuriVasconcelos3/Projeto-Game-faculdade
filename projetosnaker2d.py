import pygame as pg
from pygame.locals import *
from sys import exit
from random import randint

def main():
    pg.init()

    largura = 740
    altura = 555
    c = 0
    x = int(largura/2 - 15)
    y = int(altura/2 - 15) 

    xx = randint(30,740)
    yy = randint(30,555)
    velocidade = 10
    x_controle = velocidade
    y_controle = 0


    tela = pg.display.set_mode((largura, altura))
    pg.display.set_caption('Python na UFPE')
    relogio = pg.time.Clock()
    lista_cobra = []

    comprimento_inicial = 5

    def aumenta_cobra(lista_cobra):
        for XeY in lista_cobra:
            pg.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

    def reiniciar_jogo():
        nonlocal c, comprimento_inicial, x, y, lista_cabeça, lista_cobra, xx, yy, morreu 
        c = 0
        comprimento_inicial = 5
        x = int(largura/2 - 10)
        y = int(altura/2 - 10) 
        lista_cabeça = []
        lista_cobra = []
        xx = randint(30,740)
        yy = randint(30,555)
        morreu = False

    while True:
        tela.fill((255,255,255))
        relogio.tick(40)
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            
            if event.type == KEYDOWN:
                if event.key == K_a:
                    if x_controle == velocidade:
                        pass
                    else:
                        x_controle = -velocidade
                        y_controle = 0
                if event.key == K_d:
                    if x_controle == -velocidade:
                        pass
                    else:
                        x_controle = velocidade
                        y_controle = 0
                if event.key == K_w:
                    if y_controle == velocidade:
                        pass
                    else:
                        x_controle = 0
                        y_controle = -velocidade
                if event.key == K_s:
                    if y_controle == -velocidade:
                        pass
                    else:
                        x_controle = 0
                        y_controle = velocidade
        x = x + x_controle
        y = y + y_controle
        
        '''if pg.key.get_pressed()[K_a]:
            x = x-20
        if pg.key.get_pressed()[K_d]:
            x = x+20
        if pg.key.get_pressed()[K_w]:
            y = y-20
        if pg.key.get_pressed()[K_s]:
            y = y+20
        '''
        maça = pg.draw.rect(tela, (255, 0, 0), (xx, yy, 20, 20))
        jogador = pg.draw.rect(tela, (0, 255, 0), (x, y, 20, 20))
        
        if jogador.colliderect(maça):
            xx = randint(30,740)
            yy = randint(30,555)
            c += 1
            comprimento_inicial += 1
        lista_cabeça = []
        lista_cabeça.append(x)
        lista_cabeça.append(y)
        lista_cobra.append(lista_cabeça)

        if lista_cobra.count(lista_cabeça) > 1:
            morreu = True
            fonte = pg.font.SysFont('arial', 20, True, True) 
            mensagem = f'Tente outra vez! APERTE R PARA REINICIAR O JOGO'
            texto_formatado = fonte.render(mensagem, True, (0,0,0))
            ret_texto = texto_formatado.get_rect()
            while morreu:
                tela.fill((255,255,255))
                for event in pg.event.get():
                    if event.type == QUIT:
                        pg.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            reiniciar_jogo()
                ret_texto.center = (largura//2,altura//2)
                tela.blit(texto_formatado, ret_texto)
                pg.display.update()

        if x > largura:
            x = 0
        if x < 0:
            x = largura
        if y < 0:
            y = altura
        if y > altura:
            y = 0

        if len(lista_cobra) > comprimento_inicial:
            del lista_cobra[0]
        
        aumenta_cobra(lista_cobra)

        
        pg.display.update()
main()