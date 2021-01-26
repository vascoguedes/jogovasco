import pygame, math, random, copy
from pygame.locals import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 717
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.init()
pygame.display.set_caption("Vasco Guedes' Game")


score0 = pygame.image.load('imgs/score/0.png')
score1 = pygame.image.load('imgs/score/1.png')
score2 = pygame.image.load('imgs/score/2.png')
score3 = pygame.image.load('imgs/score/3.png')

score = {0: score0, 1: score1, 2: score2, 3: score3}
sj1 = 0
sj2 = 0
roxovence = pygame.image.load('imgs/roxovence.png')
roxovencejogo = pygame.image.load('imgs/roxovencejogo.png')
vermelhovence = pygame.image.load('imgs/vermelhovence.png')
vermelhovencejogo = pygame.image.load('imgs/vermelhovencejogo.png')

fundo = pygame.image.load('imgs/fundogrande.jpg')
bordas1 = pygame.image.load('imgs/bordasgrandes.png')
bordas2 = pygame.image.load('imgs/bordasgrandes1.png')
bordas3 = pygame.image.load('imgs/bordasgrandes2.png')
bordas4 = pygame.image.load('imgs/bordasgrandes3.png')
personagem = pygame.image.load('imgs/personagem.png')
personagemroxa = pygame.image.load('imgs/roxo.png')
personagemvermelha = pygame.image.load('imgs/vermelho.png')
personagemred = pygame.image.load('imgs/damage.png')
vermelhotransparente = pygame.image.load('imgs/vermelhotransparente.png')
roxotransparente = pygame.image.load('imgs/roxotransparente.png')

espada = pygame.image.load('imgs/espada.png')
espada1 = pygame.image.load('imgs/espada1.png')
espada2 = pygame.image.load('imgs/espada2.png')

broca = pygame.image.load('imgs/broca.png')
brocacores = pygame.image.load('imgs/brocacores.png')
broca1 = pygame.image.load('imgs/broca1.png')
broca2 = pygame.image.load('imgs/broca2.png')

flecha = pygame.image.load('imgs/flecha.png')
arco = pygame.image.load('imgs/arco.png')
arco1 = pygame.image.load('imgs/arco1.png')
arco2 = pygame.image.load('imgs/arco2.png')

pedras = pygame.image.load('imgs/pedras.png')
obstaculo = pygame.image.load('imgs/obstaculo.png')
muro = pygame.image.load('imgs/muroo.png')
muro4 = pygame.image.load('imgs/muro4.png')

poder = pygame.image.load('imgs/escudo.png')
poder1 = pygame.image.load('imgs/escudo/1.png')
poder2 = pygame.image.load('imgs/escudo/2.png')
poder3 = pygame.image.load('imgs/escudo/3.png')
poder4 = pygame.image.load('imgs/escudo/4.png')
poder5 = pygame.image.load('imgs/escudo/6.png')
escudo1 = pygame.image.load('imgs/escudo1.png')
up = pygame.image.load('imgs/up.png')

vida0 = pygame.image.load('imgs/vida0.png')
vida1 = pygame.image.load('imgs/vida1.png')
vida2 = pygame.image.load('imgs/vida2.png')
vida3 = pygame.image.load('imgs/vida3.png')
vida4 = pygame.image.load('imgs/vida4.png')
vida5 = pygame.image.load('imgs/vida5.png')
vida6 = pygame.image.load('imgs/vida6.png')
vida7 = pygame.image.load('imgs/vida7.png')
vida8 = pygame.image.load('imgs/vida8.png')
vida9 = pygame.image.load('imgs/vida9.png')
vida10 = pygame.image.load('imgs/vida10.png')
vida11 = pygame.image.load('imgs/vida11.png')
vida12 = pygame.image.load('imgs/vida12.png')
vidaextra = pygame.image.load('imgs/vidaextra.png')
particulasvida1 = pygame.image.load('imgs/death/1.png')
particulasvida2 = pygame.image.load('imgs/death/2.png')
particulasvida3 = pygame.image.load('imgs/death/3.png')
particulasvida4 = pygame.image.load('imgs/death/4.png')
particulasvida5 = pygame.image.load('imgs/death/5.png')
particulasvida6 = pygame.image.load('imgs/death/6.png')
particulasvida7 = pygame.image.load('imgs/death/7.png')

nextround = pygame.image.load('imgs/next.png')
menuopcoes = pygame.image.load('imgs/menucontrolo.png')
menuopcoes2 = pygame.image.load('imgs/menuopcoes.png')
bolinha = pygame.image.load('imgs/bolinha.png')
pocao = pygame.image.load('imgs/pocao.png')
varinha = pygame.image.load('imgs/varinha.png')

tres = pygame.image.load('imgs/countdown/3.png')
dois = pygame.image.load('imgs/countdown/2.png')
um = pygame.image.load('imgs/countdown/1.png')
go = pygame.image.load('imgs/countdown/go.png')


imavida = {0: vida0, 1: vida1, 2: vida2, 3: vida3, 4: vida4, 5: vida5, 6: vida6, 7: vida7, 8: vida8, 9: vida9, 10: vida10, 11: vida11, 12: vida12}
bolinhas = [(450,328), (550,400)]

k10 = {(0, -100, -100, -1)}
ad = 0
# condicao do objto e numero da personagem, posicao x, posicao y, temp que vai sofrer alteracao, angulo, arma, tem escudo
# Armas: nenhuma: 0; espada: 1; broca: 2, arco: 3;
"""
condicoes dos objetos:
    -1: visivel sem interacao
    0: nao visivel
    1: objeto que não é possivel passar
    2: objeto destrutivel
    3: objeto com reposicao
    4: jogador
    5: flecha

"""

clock = pygame.time.Clock()
scorejo = {0:0, 1:0}
velocidade = 0
#kk = SCREEN_WIDTH
#kk2 = SCREEN_HEIGHT
click = pygame.mixer.Sound('musicas/click.mp3')
countdown = pygame.mixer.Sound('musicas/countdown.mp3')
musicainicio = pygame.mixer.Sound('musicas/musicainicio.mp3')
musicafundo = pygame.mixer.Sound('imgs/musicafundo.mp3')
musicaarrow = pygame.mixer.Sound('musicas/arrow.mp3')
musicaespada = pygame.mixer.Sound('musicas/musicaespada.mp3')
musicabroca = pygame.mixer.Sound('musicas/musicabroca.mp3')
musicadamage = pygame.mixer.Sound('musicas/musicadamage.mp3')
musicabling = pygame.mixer.Sound('musicas/musicabling.mp3')
musicamagia = pygame.mixer.Sound('musicas/musicamagia.mp3')
musicavida = pygame.mixer.Sound('musicas/musicavida.mp3')
musicavarinha = pygame.mixer.Sound('musicas/musicavarinha.mp3')
musicashield = pygame.mixer.Sound('musicas/musicashield.mp3')
musicacountdown = pygame.mixer.Sound('musicas/countdown.mp3')
musicaininio = pygame.mixer.Sound('musicas/musicainicio.mp3')
musicafundo.play()
listamusica = [musicainicio, musicafundo, musicaarrow, musicaespada, musicabroca, musicadamage, musicabling, musicamagia, musicavida, musicavarinha, musicashield, musicacountdown, musicainicio, click]
for i in listamusica:
    i.set_volume((bolinhas[0][0] - 405) / 303)
musicafundo.set_volume((bolinhas[0][0] - 405) / 606)
def roda(i, ang):
    orig_rect = i.get_rect()
    rot_image = pygame.transform.rotate(i, ang / math.pi * 180)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    return(rot_image.subsurface(rot_rect).copy())

    
def jogo(a, b, c):
    musicafundo.stop()
    tempo = pygame.time.get_ticks()
    musicacountdown.play()
    musicafundo.play()

    z = -1
    escdown = 0
    ll = 0
    scorejo[0] = a
    scorejo[1] = b
    regras = {pedras: [],obstaculo: [], muro: [], poder: [], vidaextra: [], pocao: [], varinha: [], espada1: [], espada2: [], broca2: [], broca1: [], arco2: [], arco1: [], flecha: [], personagem : [[40, 347, 45, -1, - math.pi / 2, 0, False], [41, 848, 600, -1,   math.pi / 2, 0, False]]}
    level = {espada: [[0, 2], [1, 2], [2, 2]], flecha: [[0, 0], [1, 0], [2, 0]]}
    animacao = {espada: [[0, 0], [1, 0]], personagem: [[0, 0], [1, 0]]}
    vida = {0:10, 1: 10}
    cooldown = {0: 0, 1: 0}
    remotem = []
    upg = [0, 0]
    efeitopocao = [0, 0]
    efeitoparedes = [0, 0]
    velocidade = c
    
    
    a = [[148.5, 109.5], [148.5, 142.5], [148.5, 174.5], [148.5, 208], [181.5, 109.5], [213, 109.5], [245.5, 109.5], [278, 109.5]]
    b = [[454.5, 105.5], [454.5, 138.5], [454.5, 170.5], [454.5, 202.5], [487, 105.5], [520, 105.5], [245.5, 209], [278.5, 209], [245.5, 242]]
    c = [[16.5, 343], [50, 343], [83.5, 343], [116, 343], [149, 343], [116, 309.5], [116, 375.5], [353, 271], [353, 304], [353, 337], [353, 370.5], [353, 403.5], [386.5, 337], [420, 337], [453, 337], [486, 337]]
    d = [[620.5, 36.5], [620.5, 69.5], [620.5, 103], [620.5, 136], [620.5, 169], [620.5, 202.5], [554.5, 202.5],[587.5, 202.5],[653.5, 202.5],[687, 202.5]]
    espadas = [[194, 153]]
    brocas = [[310, 338]]
    arcos = [[475, 146]]
    
    
    for i in arcos:
        regras[arco2].append([-1, i[0] - 15.5 , i[1] - 31, -1])
        regras[arco2].append([-1, i[0] - 15.5 , 675 - i[1], -1])
        regras[arco2].append([-1, 1200 - i[0], i[1] - 31, -1])
        regras[arco2].append([-1, 1200 - i[0], 675- i[1], -1])
        regras[arco1].append([3, i[0] - 15.5 , i[1] - 31, -1])
        regras[arco1].append([3, i[0] - 15.5 , 675 - i[1], -1])
        regras[arco1].append([3, 1200 - i[0], i[1] - 31, -1])
        regras[arco1].append([3, 1200 - i[0], 675- i[1], -1])
    for i in espadas:
        regras[espada1].append([-1, i[0] - 15.5 , i[1] - 31, -1])
        regras[espada1].append([-1, i[0] - 15.5 , 675 - i[1], -1])
        regras[espada1].append([-1, 1200 - i[0], i[1] - 31, -1])
        regras[espada1].append([-1, 1200 - i[0], 675- i[1], -1])
        regras[espada2].append([3, i[0] - 15.5 , i[1] - 31, -1])
        regras[espada2].append([3, i[0] - 15.5 , 675 - i[1], -1])
        regras[espada2].append([3, 1200 - i[0], i[1] - 31, -1])
        regras[espada2].append([3, 1200 - i[0], 675- i[1], -1]) 
    for i in brocas:
        regras[broca1].append([3, i[0] - 15.5 , i[1] - 31, -1])
        regras[broca1].append([3, 1200-  i[0], i[1] - 31, -1])
        regras[broca2].append([-1, i[0] - 15.5 , i[1] - 31, -1])
        regras[broca2].append([-1, 1200-  i[0], i[1] - 31, -1])
    for i in a:
        regras[obstaculo].append([2, i[0] - 16.5, i[1] - 33, -1])
        regras[obstaculo].append([2, i[0] - 16.5, 675 - i[1], -1])
        regras[obstaculo].append([2, 1200 - i[0] , 675 - i[1], -1])
        regras[obstaculo].append([2, 1200 - i[0] , i[1] - 33, -1])
        regras[pedras].append([-1, i[0] - 16.5, i[1] - 33, -1])
        regras[pedras].append([-1, i[0] - 16.5, 675 - i[1], -1])
        regras[pedras].append([-1, 1200 - i[0] , 675 - i[1], -1])
        regras[pedras].append([-1, 1200 - i[0] , i[1] - 33, -1])
    for i in b:
        regras[muro].append([1, i[0] - 36.5, i[1] - 33, -1])
        regras[muro].append([1, i[0] - 36.5, 675 - i[1], -1])
        regras[muro].append([1, 1200 - i[0] + 20 , 675 - i[1], -1])
        regras[muro].append([1, 1200 - i[0] + 20 , i[1] - 33, -1])
    for i in c:
        regras[obstaculo].append([2, i[0] - 16.5, i[1] - 33, -1])
        regras[obstaculo].append([2, 1200 - i[0] , i[1] - 33, -1])
        regras[pedras].append([-1, i[0] - 16.5, i[1] - 33, -1])
        regras[pedras].append([-1, 1200 - i[0] , i[1] - 33, -1])
    for i in d:
        regras[obstaculo].append([2, i[0] - 16.5, i[1] - 33, -1])
        regras[obstaculo].append([2, i[0] - 16.5, 675 - i[1], -1])
        regras[pedras].append([-1, i[0] - 16.5, i[1] - 33, -1])
        regras[pedras].append([-1, i[0] - 16.5, 675 - i[1], -1])
    tictac = 0
    running = True
    while running:
        if z != -1:
            return (z, velocidade)
        clock.tick(100)
        k = copy.deepcopy(list(regras[personagem])[0])
        
        #ler eventos
        lista = pygame.event.get()
        for ev in lista:
            if ev.type == pygame.QUIT:
                escdown = 1
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    escdown = 1
                
                
        if pygame.key.get_pressed()[pygame.K_d]: 
            regras[personagem][0][4] -= math.pi / 40
        if pygame.key.get_pressed()[pygame.K_a]:
            regras[personagem][0][4] += math.pi / 40
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            regras[personagem][1][4] += math.pi / 40
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            regras[personagem][1][4] -= math.pi / 40
        n = 0
        for i in regras[flecha]:
            if i[0] == 50:
                n += 1
        n1 = 0
        for i in regras[flecha]:
            if i[0] == 51:
                n1 += 1
        #corrigir isto 
        for ev in lista:
            if pygame.key.get_pressed()[pygame.K_w] and regras[personagem][0][5] == 3 and regras[personagem][0][0] != 0 and n < level[flecha][0][1]:
                musicaarrow.play()
                regras[flecha].append([50, regras[personagem][0][1] + (personagem.get_width() + 2 * math.cos(regras[personagem][0][4])) * math.cos(regras[personagem][0][4]) * 1.3 , regras[personagem][0][2] + (-1.3) * (personagem.get_height() + 2 * math.sin(regras[personagem][0][4])) * math.sin(regras[personagem][0][4]), regras[personagem][0][4]])
            if pygame.key.get_pressed()[pygame.K_w] and regras[personagem][0][5] == 1 and regras[personagem][0][0] != 0 and animacao[espada][0][0] == 0:
                animacao[espada][0][1] = 100
                musicaespada.play()
            if pygame.key.get_pressed()[pygame.K_UP] and regras[personagem][1][5] == 1 and regras[personagem][1][0] != 0 and animacao[espada][1][1] == 0:
                animacao[espada][1][1] = 100
                musicaespada.play()
            if pygame.key.get_pressed()[pygame.K_UP] and regras[personagem][1][5] == 3 and regras[personagem][1][0] != 0 and n1 < level[flecha][1][1]:
                musicaarrow.play()
                regras[flecha].append([51, regras[personagem][1][1] + (personagem.get_width() + 2 * math.cos(regras[personagem][0][4])) * math.cos(regras[personagem][1][4]) * 1.3 , regras[personagem][1][2] + (-1.3) * (personagem.get_height() + 2 * math.sin(regras[personagem][0][4])) * math.sin(regras[personagem][1][4]), regras[personagem][1][4]])
    
        #logica (fisica)
        def nocoli(obj, tx, ty):
            if obj == personagem or obj == espada or obj == flecha:
                numpers1 = tx
                tx = ty[0]
                ty = ty[1]
            rect1 = pygame.Rect(tx, ty, obj.get_width(), obj.get_height())
            for ii in regras:
                for i in regras[ii]:
                    if ii == personagem:
                        (cond, x, y, temp, ang, arma, escd) = i
                        numpers2 = cond % 10
                        cond = cond // 10
                    elif ii == flecha:
                        (cond, x, y, ang) = i
                        numpers2 = cond % 10
                        cond = cond // 10
                    else:
                        (cond, x, y, temp) = i
                    
                    rect2 = pygame.Rect(x, y, ii.get_width(), ii.get_height())
                    
                    #efeito paredes
                    if obj == personagem and efeitoparedes[numpers1] > 0:
                        return True
                    
                    #objetos que nao permitem passar
                    if cond == 1 and rect1.colliderect(rect2):
                        return False

                    # colisao com desaparecimento do objeto
                    if (obj == personagem or obj == flecha) and cond == 2 and rect1.colliderect(rect2):
                        if obj == flecha:
                            if ii == poder:
                                return True
                            else:
                                return False 
                        
                        if ii == poder:
                            musicashield.play()
                            regras[personagem][numpers1][6] = True
                            regras[ii].remove(i)
                            return True
                        if ii == vidaextra:
                            musicavida.play()
                            vida[numpers1] += ((12 - vida[numpers1]) if vida[numpers1] > 8 else 4)
                            regras[ii].remove(i)
                            return True
                        if regras[personagem][numpers1][5] == 2:
                            if (numpers1 == 0 and pygame.key.get_pressed()[pygame.K_w]) or (numpers1 == 1 and pygame.key.get_pressed()[pygame.K_UP]):
                                regras[ii].remove(i)
                                return True
                        if ii == pocao:
                            musicamagia.play()
                            efeitopocao[numpers1] += 100
                            regras[ii].remove(i)
                            return True
                        if ii == varinha:
                            musicavarinha.play()
                            efeitoparedes[numpers1] += 100
                            regras[ii].remove(i)
                            return True
                        return False
                    
                    # colisao com reposicao do objeto
                    if obj == personagem and cond == 3 and rect1.colliderect(rect2):
                        i[0] = 0
                        i[3] = 1000
                        if ii == broca1:
                            regras[personagem][numpers1][5] = 2
                            level[flecha][numpers1][1] = 0
                            level[espada][numpers1][1] = 2
                        elif ii == espada2:
                            if regras[personagem][numpers1][5] == 1 and level[espada][numpers1][1] < 5: 
                                upg[numpers1] = 10
                            else:
                                regras[personagem][numpers1][5] = 1
                            if level[espada][numpers1][1] < 5:
                                musicabling.play() if level[espada][numpers1][1] > 2 else None
                                level[espada][numpers1][1] += 1
                            level[flecha][numpers1][1] = 0
                        elif ii == arco1:
                            if regras[personagem][numpers1][5] == 3 and level[flecha][numpers1][1] < 3: 
                                upg[numpers1] = 10
                            else:
                                regras[personagem][numpers1][5] = 3
                            level[espada][numpers1][1] = 2
                            if level[flecha][numpers1][1] < 3:
                                musicabling.play() if level[flecha][numpers1][1] > 0 else None
                                level[flecha][numpers1][1] += 1
                        return False
                    
                    # colisão objeto objeto
                    if obj == poder and rect1.colliderect(rect2):
                        return False
                    
                    # colisao pessoa com pessoa
                    if (obj == personagem or obj == espada) and cond == 4 and numpers1 != numpers2 and rect1.colliderect(rect2) and efeitopocao[numpers2] <= 0 :
                        if (regras[personagem][numpers1][5] == 1 or regras[personagem][numpers1][5] == 2) and cooldown[numpers2] == 0:
                            musicadamage.play()
                            cooldown[numpers2] = 400
                            regras[personagem][numpers2][0] -= 40
                            if regras[personagem][numpers2][6] == True:
                                regras[personagem][numpers2][6] = False
                                if obj == espada:
                                    animacao[espada][numpers1][1] = 0
                                return False
                    
                            else:
                                vida[numpers2] -= level[espada][numpers1][1] if regras[personagem][numpers1][5] == 1 else 2
                                if obj == espada:
                                    animacao[espada][numpers1][1] = 0
                                if vida[numpers2] <= 0:
                                    regras[personagem][numpers2][0] = numpers2
                                    z = numpers1
                                return False
                        else:
                            return False
                    elif obj == personagem and ii == personagem and rect1.colliderect(rect2) and numpers1 != numpers2:
                        return False
                        
                    # colisao flecha com pessoa
                    if obj == flecha and cond == 4 and rect1.colliderect(rect2) and cooldown[numpers2] == 0:
                        musicadamage.play()
                        cooldown[numpers2] = 400
                        regras[personagem][numpers2][0] -= 40
                        if regras[personagem][numpers2][6] == True:
                            regras[personagem][numpers2][6] = False
                            return False
                        else:
                            vida[numpers2] -= level[flecha][numpers1][1]
                            if vida[numpers2] <= 0:
                                regras[personagem][numpers2][0] = numpers2
                                z = numpers1
                            return False
            
            return True
        
        # movimento do boneco
        
        #atualizaposi(kk, kk2)
        for i in range(len(regras[personagem])):
            y = regras[personagem][i]
            if math.cos(y[4]) != 0 and y[1] + math.cos(y[4]) * velocidade < (SCREEN_WIDTH - 15 -personagem.get_width()) and y[1] + math.cos(y[4]) * velocidade > 15 and nocoli(personagem, y[0] % 10 ,[y[1] + math.cos(y[4]) * velocidade, y[2]]):
                regras[personagem][i] = [y[0], y[1] + math.cos(y[4]) * velocidade, y[2], y[3], y[4], y[5], y[6]]
            
            y = regras[personagem][i]
        
            if y[2] - math.sin(y[4]) * velocidade > 13 and y[2] - math.sin(y[4]) * velocidade < SCREEN_HEIGHT - 57 - personagem.get_height() and math.sin(y[4]) != 0 and nocoli(personagem, y[0] % 10 ,[y[1], y[2] - math.sin(y[4]) * velocidade]):
                regras[personagem][i] = [y[0], y[1], y[2] - math.sin(y[4]) * velocidade, y[3], y[4], y[5], y[6]]
        
        # movimento das flechas
        
        remo = set()
        for i in range(len(regras[flecha])):
            y = regras[flecha][i]
            if math.cos(y[3]) != 0 and y[1] + math.cos(y[3]) < (SCREEN_WIDTH - 15 - flecha.get_width()) and y[1] + math.cos(y[3]) > 15 and nocoli(flecha, y[0] % 10, ( y[1] + math.cos(y[3]) * 2.5 * velocidade , y[2])):
                regras[flecha][i] = [y[0], y[1] + math.cos(y[3]) * 2.5 * velocidade, y[2], y[3]]
            else:
                remo.add(i)
            
            y = regras[flecha][i]
        
            if y[2] - math.sin(y[3]) > 13 and y[2] - math.sin(y[3]) < SCREEN_HEIGHT - 75 - flecha.get_height() and math.sin(y[3]) != 0 and nocoli(flecha, y[0] % 10, ( y[1], y[2] - math.sin(y[3]) * 2.5 * velocidade)):
                regras[flecha][i] = [y[0], y[1], y[2] - math.sin(y[3]) * 2.5 * velocidade, y[3]]
            else:
                remo.add(i)
                
        remo = sorted(remo, key = lambda x: -x)
        #corrigir flechas
        for i in remo:
            remotem.append([copy.deepcopy(regras[flecha][i]), 100])
            regras[flecha].pop(i)
            
    
        #desenhar
    
        screen_info = pygame.display.Info()   
        
        #obstaculo = pygame.transform.scale(obstaculo, (int(obstaculo.get_width() * (kk / screen_info.current_w)) , int(obstaculo.get_height() * (kk2 / screen_info.current_h))))
        
        screen.blit(fundo, (0,0))
    
        
        # aparecimento dos poderes
        
        tictac += 1
        if tictac % 1000 == 0 and len(regras[poder] + regras[vidaextra] + regras[varinha] + regras[pocao]) <= 1:
            bug = False
            while bug == False:
                x1 = random.randrange(50, SCREEN_WIDTH - 50)
                y1 = random.randrange(50, SCREEN_HEIGHT - 100)
                bug = nocoli(poder, x1, y1)
            
            rando = random.randrange(0, 4)
            if rando == 0:
                regras[poder].append([2, x1, y1, -1])
                cooldown[poder] = 100
            elif rando == 1:
                regras[vidaextra].append([2, x1, y1, -1])
            elif rando == 2:
                regras[pocao].append([2, x1, y1, -1])
            elif rando == 3:
                regras[varinha].append([2, x1, y1, -1])
                
        #imprimir obstaculos e isso do mapa
        
        for i in regras:
            for ii in regras[i]:
                if not i in [personagem, flecha, poder]:
                    (cond, x3, y3, temp) = ii
                    if cond != 0 :
                            screen.blit(i, (x3, y3))
                if i == poder:
                    (cond, x3, y3, temp) = ii
                    cooldown[poder] -= 1
                    if cooldown[poder] in range (100, 80, -1):
                        screen.blit(poder1, (x3, y3))
                    elif cooldown[poder] in range (80, 60, -1):
                        screen.blit(poder2, (x3, y3))
                    elif cooldown[poder] in range (60, 40, -1):
                        screen.blit(poder3, (x3, y3))
                    elif cooldown[poder] in range (40, 20, -1):
                        screen.blit(poder4, (x3, y3))
                    else:
                        screen.blit(poder5, (x3, y3))
                        
                        
        screen.blit(bordas1, (0,0))
        screen.blit(bordas2, (0,0))
        screen.blit(bordas3, (0, 653))
        screen.blit(bordas4, (1175, 0))
            
        for i in regras[flecha]:
            (cond, x3, y3, ang) = i
    
            screen.blit(pygame.transform.rotate(flecha, ang / math.pi * 180), (x3, y3))
    
        for i in range(len(remotem)):
            if remotem[i][1] <= 0:
                remotem.pop(i)
                break
                
        for i in range(len(remotem)):
            remotem[i][1] -= 1
            (cond, x3, y3, ang) = remotem[i][0]
            screen.blit(pygame.transform.rotate(flecha, ang / math.pi * 180), (x3, y3))
        
        # blit personagens
        
        for i in regras:
            for ii in regras[i]:
                if i == personagem:
                    (cond, x3, y3, temp, ang, arma, escd) = ii
                    np = cond % 10
    
                    if cond != -1:
                        if cooldown[np] <= 0:
                             #or cooldown[np] in range (160, 120, -1) or cooldown[np] in range(80, 40, -1) or cooldown[np] in range(20, 0, -1)
                            regras[personagem][np][0] = 40 + np
                            if efeitoparedes[np] > 0 and efeitopocao[np] > 0:
                                efeitopocao[np] -= 0.2
                                lo = copy.deepcopy(efeitoparedes[np])
                                efeitoparedes[np] = 0
                                if nocoli(personagem, np, [x3, y3]):
                                    efeitoparedes[np] -= 0.2
                                efeitoparedes[np] += lo
                                screen.blit(pygame.transform.scale(roda(vermelhotransparente , ang), (40, 40)), (x3, y3)) if np == 1 else screen.blit(pygame.transform.scale(roda(roxotransparente , ang), (40, 40)), (x3, y3))
                                
                            elif efeitopocao[np] > 0:
                                efeitopocao[np] -= 0.2
                                screen.blit(pygame.transform.scale(roda(personagemvermelha, ang), (40, 40)), (x3, y3)) if np == 1 else screen.blit(pygame.transform.scale(roda(personagemroxa, ang), (40, 40)), (x3, y3))
                            elif efeitoparedes[np] > 0:
                                lo = copy.deepcopy(efeitoparedes[np])
                                efeitoparedes[np] = 0
                                if nocoli(personagem, np, [x3, y3]):
                                    efeitoparedes[np] -= 0.2
                                efeitoparedes[np] += lo
                                screen.blit(roda(vermelhotransparente, ang), (x3, y3)) if np == 1 else screen.blit(roda(roxotransparente, ang), (x3, y3))
                                
                            else:
                                screen.blit(roda(personagemvermelha, ang), (x3, y3)) if (np == 1 and vida[1] > 0) else screen.blit(roda(personagemroxa, ang), (x3, y3)) if (np == 0 and vida[0] > 0) else None        
                                
                        if (cooldown[np] in range (360, 300, -1)) or (cooldown[np] in range(240, 160, -1)) or (cooldown[np] in range( 80, 40, -1)):
                            screen.blit(roda(personagemred, ang), (x3, y3))
                        elif cooldown[np] != 0:
                            screen.blit(roda(vermelhotransparente, ang), (x3, y3)) if np == 1 else screen.blit(roda(roxotransparente, ang), (x3, y3))
                        if cooldown[np] > 295:
                            screen.blit(roda(particulasvida1 if cooldown[np] > 380 else particulasvida2 if cooldown[np] > 360 else particulasvida3 if cooldown[np] > 340 else particulasvida4 if cooldown[np] > 325 else particulasvida5 if cooldown[np] > 310 else particulasvida6 if cooldown[np] > 295 else particulasvida7 if cooldown[np] > 265 else None, ang), (x3, y3))
                        
                        #para a arma
                        rot_image = pygame.transform.scale(roda(espada, ang), ((40, 40) if efeitopocao[np] > 0 else (34, 34)))
                        if arma == 1:
                            if animacao[espada][np][1] > 50:
                                animacao[espada][np][1] -= 2
                                screen.blit(rot_image, (x3 + (100 - animacao[espada][np][1]) * math.cos(ang), y3 - (100 - animacao[espada][np][1]) * math.sin(ang)))
                                
                                nocoli(espada, np, (x3 + (100 - animacao[espada][np][1]) * math.cos(ang), y3 - (100 - animacao[espada][np][1]) * math.sin(ang)))
                            elif animacao[espada][np][1] > 0:
                                animacao[espada][np][1] -= 2
                                screen.blit(rot_image, (x3 + (animacao[espada][np][1]) * math.cos(ang), y3 - (animacao[espada][np][1]) * math.sin(ang)))
                                
                                nocoli(espada, np ,((animacao[espada][np][1]) * math.cos(ang), y3 - (animacao[espada][np][1]) * math.sin(ang)))
                            else:
                                screen.blit(rot_image, (x3, y3))
                        
                        #para a broca
                        rot_image = pygame.transform.scale(roda(broca, ang), ((40, 40) if efeitopocao[np] > 0 else (34, 34)))
                        
                        #para a brocacores
                        rot_image1 = pygame.transform.scale(roda(brocacores, ang), ((40, 40) if efeitopocao[np] > 0 else (34, 34)))
                        
                        if arma == 2:
                            if (pygame.key.get_pressed()[pygame.K_UP] and np == 1) or (pygame.key.get_pressed()[pygame.K_w] and np == 0):
                                musicabroca.play()
                                screen.blit(rot_image1, (x3, y3))
                            else:
                                screen.blit(rot_image, (x3, y3))
                        
                        #para o arco
                        rot_image = pygame.transform.scale(roda(arco, ang), ((40, 40) if efeitopocao[np] > 0 else (34, 34)))
                        if arma == 3:
                            screen.blit(rot_image, (x3, y3))
                        
                        #para o escudo
                        rot_image = pygame.transform.scale(roda(escudo1, ang), ((40, 40) if efeitopocao[np] > 0 else (34, 34)))
                        if escd == True:
                            screen.blit(rot_image, (x3, y3))
                            
                        if upg[np] > 0:
                            screen.blit(up, (x3, y3 + upg[np]))
                            upg[np] -= 0.4 
                        

        for i in regras:
            for ii in regras[i]:
                if i == personagem:
                    cond1, x2, y2, temp, ang, arma, escd = ii
                elif i != flecha:
                    cond1, x2, y2, temp = ii
                    if temp > 0 and not temp in [300, 200, 100, 50, 0]:
                        ii[3] -= 1
                    if temp == 300 or temp == 100:
                        ii[0] = -1
                        ii[3] -= 1
                    elif temp == 200 or temp == 50:
                        ii[0] = 0
                        ii[3] -= 1
                    elif temp == 0 :
                        ii[0] = 3
                        ii[3] -= 1
        cooldown[0] -= (1 if cooldown[0] != 0 else 0)
        cooldown[1] -= (1 if cooldown[1] != 0 else 0)
        
        screen.blit(imavida[vida[0]], (270,665)) if vida[0] > 0 else screen.blit(imavida[0], (270,665))
        screen.blit(imavida[vida[1]], (785,665)) if vida[1] > 0 else screen.blit(imavida[0], (785,665))
        
        screen.blit(score[scorejo[0]], (572,667))
        screen.blit(score[scorejo[1]], (635,667))
        if vida[0] <= 0 or vida[1] <= 0:
            screen.blit(nextround, (470, 400))
            if vida[1] <= 0:
                screen.blit(roxovence, (435, 150))
            else:
                screen.blit(vermelhovence, (250, 150))
            ll = 0
            while ll == 0:
                pygame.display.flip()
                lista = pygame.event.get()
                for ev in lista:
                    if ev.type == pygame.MOUSEBUTTONUP:
                        (x22, y22) = pygame.mouse.get_pos()
                        if y22 >= 400 and y22 <= 475 and x22 >= 470 and x22 <= 740:
                            ll = 1
                            return (1, velocidade) if vida[0] <= 0 else (0, velocidade)
                            
        if escdown == 1:
            screen.blit(menuopcoes, (385, 214))
            pygame.display.flip()
            while escdown == 1:
                lista = pygame.event.get()
                for ev in lista:
                    if ev.type == pygame.MOUSEBUTTONUP:
                        (x22, y22) = pygame.mouse.get_pos()
                        if y22 >= 220 and y22 <= 294 and x22 >= 393 and x22 <= 813:
                            escdown = 0
                            click.play()
                        elif y22 >= 303 and y22 <= 390 and x22 >= 393 and x22 <= 524:
                            click.play()
                            return (3, velocidade)
                        elif y22 >= 303 and y22 <= 390 and x22 >= 533 and x22 <= 664:
                            click.play()
                            return (4, velocidade)
                        elif y22 >= 303 and y22 <= 390 and x22 >= 673 and x22 <= 804:
                            click.play()
                            return (2, velocidade)
                        elif y22 >= 399 and y22 <= 450 and x22 >= 393 and x22 <= 813:
                            click.play()
                            lo = opcoes(velocidade)
                            if lo[0] == 1:
                                return(2, lo[1])
                            elif lo[0] == 2:
                                escdown = 0
                            if velocidade != lo[1]:
                                velocidade = lo[1]
                    elif ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_ESCAPE:
                            escdown = 0
                    elif ev.type == pygame.QUIT:
                        return (2, velocidade)

        while pygame.time.get_ticks() <= tempo + 900 and pygame.time.get_ticks() > tempo:
            lista = pygame.event.get()
            velocidade = 0
            screen.blit(tres, (550, 240))
            pygame.display.flip()
        while pygame.time.get_ticks() <= tempo + 1800 and pygame.time.get_ticks() > tempo + 902:
            lista = pygame.event.get()
            screen.blit(dois, (550, 240))
            pygame.display.flip()
        while pygame.time.get_ticks() <= tempo + 2800 and pygame.time.get_ticks() > tempo + 1802:
            lista = pygame.event.get()
            screen.blit(um, (550, 240))
            pygame.display.flip()
            velocidade = ((bolinhas[1][0] -405) /303) * 4
        if pygame.time.get_ticks() <= tempo + 3800 and pygame.time.get_ticks() > tempo + 2802:
            musicainicio.play()
            screen.blit(go, (445, 240))
            lista = pygame.event.get()
        pygame.display.flip()
        
def opcoes(velocidade):
    screen.blit(menuopcoes2, (385, 214))
    pygame.display.flip()
    ll = 0
    while ll == 0:
        screen.blit(menuopcoes2, (385, 214))
        screen.blit(bolinha, bolinhas[0])
        screen.blit(bolinha, bolinhas[1])
        lista = pygame.event.get()
        if pygame.mouse.get_pressed()[0]:
                (x22, y22) = pygame.mouse.get_pos()
                if y22 >= 220 and y22 <= 264 and x22 >= 779 and x22 <= 823:
                    ll = 1
                    escdown = 0
                if y22 >= bolinhas[1][1] - bolinha.get_height() and y22 <= bolinhas[1][1] + bolinha.get_height() and x22 >= bolinhas[1][0] - bolinha.get_width() and x22 <= bolinhas[1][0] + bolinha.get_width():
                    lista = pygame.event.get()
                    while pygame.mouse.get_pressed()[0]:
                        (x22, y22) = pygame.mouse.get_pos()
                        screen.blit(menuopcoes2, (385, 214))
                        screen.blit(bolinha, bolinhas[0])
                        if x22 > 795:
                            x22 = 795
                        elif x22 < 420:
                            x22 = 420
                        bolinhas[1] = (x22 - 15, bolinhas[1][1])
                        velocidade = ((bolinhas[1][0] - 405) / 303) * 4
                        screen.blit(bolinha, bolinhas[1])
                        pygame.display.flip()
                        lista = pygame.event.get()
                elif y22 >= bolinhas[0][1] - bolinha.get_height() and y22 <= bolinhas[0][1] + bolinha.get_height() and x22 >= bolinhas[0][0] - bolinha.get_width() and x22 <= bolinhas[0][0] + bolinha.get_width():
                    lista = pygame.event.get()
                    while pygame.mouse.get_pressed()[0]:
                        (x22, y22) = pygame.mouse.get_pos()
                        screen.blit(menuopcoes2, (385, 214))
                        screen.blit(bolinha, bolinhas[1])
                        if x22 > 795:
                            x22 = 795
                        elif x22 < 420:
                            x22 = 420
                        bolinhas[0] = (x22 - 15, bolinhas[0][1])
                        for i in listamusica:
                            i.set_volume((bolinhas[0][0] - 405) / 303)
                        musicafundo.set_volume((bolinhas[0][0] - 405) / 606)
                        screen.blit(bolinha, bolinhas[0])
                        pygame.display.flip()
                        lista = pygame.event.get()
        for ev in lista:
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    return (2, velocidade)
            elif ev.type == pygame.QUIT:
                return (1, velocidade)
        pygame.display.flip()
    return (0, velocidade)
    

def menu(velocidade):
    tictac = 0
    runmenu = True
    #items menu
    fundomenu = pygame.image.load('menu/fundomenu.png')
    ani1 = pygame.image.load('menu/animacao/1.png')
    ani2 = pygame.image.load('menu/animacao/2.png')
    ani3 = pygame.image.load('menu/animacao/3.png')
    while runmenu:
        #eventos
        
        lista = pygame.event.get()
        for ev in lista:
            if ev.type == pygame.QUIT:
                runmenu = False
                return (-1, velocidade)
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    runmenu = False
                    return (-1, velocidade)
            elif ev.type == pygame.MOUSEBUTTONUP:
                (x22, y22) = pygame.mouse.get_pos()
                if x22 >= 525 and x22 <= 1110 and y22 >= 470 and y22 <= 560:
                    click.play()
                    runmenu = False
                    return(0, velocidade)
                elif x22 >= 820 and x22 <= 1110 and y22 >= 575 and y22 <= 665:
                    click.play()
                    runmenu = False
                    return (-1, velocidade)
                elif x22 >= 525 and x22 <= 815 and y22 >= 575 and y22 <= 660:
                    click.play()
                    lo = opcoes(velocidade)
                    velocidade = lo[1]
                    click.play()
                    if lo[0] == 1:
                        return (-1, velocidade)
                
                    
        tictac += 1
        
        #imagens
        screen_info = pygame.display.Info()
         
        fundomenu = pygame.transform.scale(fundomenu, (screen_info.current_w, screen_info.current_h))
        ani1 = pygame.transform.scale(ani1, (screen_info.current_w, screen_info.current_h))
        ani2 = pygame.transform.scale(ani2, (screen_info.current_w, screen_info.current_h))
        ani3 = pygame.transform.scale(ani3, (screen_info.current_w, screen_info.current_h))
    
        screen.blit(fundomenu, (0,0))
        
        if tictac % 60 in range(0, 15):
            screen.blit(ani1, (0,0))
        elif tictac % 60 in range(15, 30):
            screen.blit(ani2, (0,0))
        elif tictac % 60 in range(30, 45):
            screen.blit(ani3, (0,0))
        elif tictac % 60 in range(45, 60):
            screen.blit(ani2, (0,0))
    
        
        pygame.display.flip()
        
jogar = 1
while jogar == 1:
    sco = [0,0]    
    lo = menu(velocidade)
    velocidade = lo[1]
    if lo[0] == -1:
        sco[0] = 1000
        jogar = 0
#0 vencedor 0 ganha, 1 jogador 1 ganha, 2 sair do jogo, 3 recomeçar ronda, 4 Menu, 5 opcões
    while (sco[0] + sco[1]) < 3:
        a = jogo(sco[0], sco[1], velocidade)
        velocidade = a[1]
        a = a[0]
        if a == 0:
            sco[0] += 1
        elif a == 1:
            sco[1] += 1
        elif a == 2:
            jogar = 0
            break
        elif a == 3:
            continue
        elif a == 4:
            break
        elif a == 5:
            continue
    lo1 = 0
    while lo1 == 0 and sum(sco) == 3:
        screen.blit(roxovencejogo if sco[0] in [2, 3] else vermelhovencejogo, (0, 0))
        pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONUP:
                (x22, y22) = pygame.mouse.get_pos()
                if x22 >= 325 and x22 <= 875 and y22 >= 515 and y22 <= 590:
                    lo1 = 1
            elif ev.type == pygame.QUIT:
                lo1 = 1
                jogar = 0
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    lo1 = 1
                    jogar = 0
                
        
        
        
# corrigir tempo de cooldown
pygame.quit()
