import pygame, math, random, copy
from pygame.locals import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 717
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.init()
pygame.display.set_caption("Vasco Guedes' Game")

#items menu
fundomenu = pygame.image.load('menu/fundomenu.png')
ani1 = pygame.image.load('menu/animacao/1.png')
ani2 = pygame.image.load('menu/animacao/2.png')
ani3 = pygame.image.load('menu/animacao/3.png')

fundo = pygame.image.load('imgs/fundogrande.jpg')
bordas = pygame.image.load('imgs/bordasgrandes.png')
personagem = pygame.image.load('imgs/personagem.png')
personagemred = pygame.image.load('imgs/damage.png')

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

imavida = {0: vida0, 1: vida1, 2: vida2, 3: vida3, 4: vida4, 5: vida5, 6: vida6, 7: vida7, 8: vida8, 9: vida9, 10: vida10}

k10 = {(0, -100, -100, -1)}
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

tictac = 0
clock = pygame.time.Clock()
#clock.tick(30)
#kk = SCREEN_WIDTH
#kk2 = SCREEN_HEIGHT

regras = {pedras: [],obstaculo: [], muro: [], poder: [], espada1: [], espada2: [], broca2: [], broca1: [], arco2: [], arco1: [], flecha: [], personagem : [[40, 347, 45, -1, - math.pi / 2, 0, False], [41, 848, 600, -1,   math.pi / 2, 0, False]]}
level = {espada: [[0, 3], [1, 3], [2, 3]], flecha: [[0, 0], [1, 0], [2, 0]]}
animacao = {espada: [[0, 0], [1, 0]], personagem: [[0, 0], [1, 0]]}
vida = {0:10, 1: 10}
cooldown = {0: 0, 1: 0}
remotem = []

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
"""
def atualizaposi(kk, kk2):
    for i in regras:
        for ii in range(len(regras[i])):
            regras[i][ii][1] = (regras[i][ii][1] / kk) * screen_info.current_w 
            regras[i][ii][2] = (regras[i][ii][2] / kk2) * screen_info.current_h
    return None
"""
def roda(i, ang):
    orig_rect = i.get_rect()
    rot_image = pygame.transform.rotate(i, ang / math.pi * 180)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    return(rot_image.subsurface(rot_rect).copy())
    
ad = 0

runmenu = True
while runmenu:
    #eventos
    
    lista = pygame.event.get()
    for ev in lista:
        if ev.type == pygame.QUIT:
            runmenu = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                runmenu = False
                
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
    
running = True
while running:
    k = copy.deepcopy(list(regras[personagem])[0])
    
    #ler eventos
    lista = pygame.event.get()
    for ev in lista:
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                running = False
            
            if pygame.key.get_pressed()[pygame.K_RIGHT]: 
                regras[personagem][0][4] -= math.pi / 32
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                regras[personagem][0][4] += math.pi / 32
            if pygame.key.get_pressed()[pygame.K_a]:
                regras[personagem][1][4] += math.pi / 32
            if pygame.key.get_pressed()[pygame.K_d]:
                regras[personagem][1][4] -= math.pi / 32
            n = 0
            for i in regras[flecha]:
                if i[0] == 50:
                    n += 1
            n1 = 0
            for i in regras[flecha]:
                if i[0] == 51:
                    n1 += 1
            if pygame.key.get_pressed()[pygame.K_UP] and regras[personagem][0][5] == 3 and regras[personagem][0][0] != 0 and n < level[flecha][0][1]:
                regras[flecha].append([50, regras[personagem][0][1] + (personagem.get_width() + 5) * math.cos(regras[personagem][0][4]) * 1.3 , regras[personagem][0][2] + (-1.3) * (personagem.get_height() + 5) * math.sin(regras[personagem][0][4]), regras[personagem][0][4]])
            if pygame.key.get_pressed()[pygame.K_UP] and regras[personagem][0][5] == 1 and regras[personagem][0][0] != 0 and animacao[espada][0][0] == 0:
                animacao[espada][0][1] = 100
            if pygame.key.get_pressed()[pygame.K_w] and regras[personagem][1][5] == 1 and regras[personagem][1][0] != 0 and animacao[espada][1][1] == 0:
                animacao[espada][1][1] = 100
            if pygame.key.get_pressed()[pygame.K_w] and regras[personagem][1][5] == 3 and regras[personagem][1][0] != 0 and n1 < level[flecha][1][1]:
                regras[flecha].append([51, regras[personagem][1][1] + (personagem.get_width() + 5) * math.cos(regras[personagem][1][4]) * 1.3 , regras[personagem][1][2] + (-1.3) * (personagem.get_height() + 5) * math.sin(regras[personagem][1][4]), regras[personagem][1][4]])

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
                
                #objetos que nao permitem passar
                rect2 = pygame.Rect(x, y, ii.get_width(), ii.get_height())
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
                        regras[personagem][numpers1][6] = True
                        regras[ii].remove(i)
                        return True
                    if regras[personagem][numpers1][5] == 2:
                        if (numpers1 == 0 and pygame.key.get_pressed()[pygame.K_UP]) or (numpers1 == 1 and pygame.key.get_pressed()[pygame.K_w]):
                            regras[ii].remove(i)
                            return True
                    return False
                
                # colisao com reposicao do objeto
                if obj == personagem and cond == 3 and rect1.colliderect(rect2):
                    i[0] = 0
                    i[3] = 1000
                    if ii == broca1:
                        regras[personagem][numpers1][5] = 2
                    elif ii == espada2:
                        regras[personagem][numpers1][5] = 1
                        if level[espada][numpers1][1] < 5:
                            level[espada][numpers1][1] += 1
                        level[flecha][numpers1][1] = 0
                    elif ii == arco1:
                        regras[personagem][numpers1][5] = 3
                        if level[flecha][numpers1][1] < 3:
                            level[flecha][numpers1][1] += 1
                    return False
                
                # colisão objeto objeto
                if obj == poder and rect1.colliderect(rect2):
                    return False
                
                # colisao pessoa com pessoa
                if (obj == personagem or obj == espada) and cond == 4 and numpers1 != numpers2 and rect1.colliderect(rect2):
                    if (regras[personagem][numpers1][5] == 1 or regras[personagem][numpers1][5] == 2) and cooldown[numpers2] == 0:
                        cooldown[numpers2] = 200
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
                                regras[personagem][numpers2][0] = 0
                            return True
                    else:
                        return False
                    
                # colisao flecha com pessoa
                if obj == flecha and cond == 4 and rect1.colliderect(rect2) and cooldown[numpers2] == 0:
                    cooldown[numpers2] = 200
                    regras[personagem][numpers2][0] -= 40
                    if regras[personagem][numpers2][6] == True:
                        regras[personagem][numpers2][6] = False
                        return False
                    else:
                        vida[numpers2] -= level[flecha][numpers1][1]
                        if vida[numpers2] <= 0:
                            regras[personagem][numpers2][0] = 0
                        return False
                
        return True
    # movimento do boneco
    #atualizaposi(kk, kk2)
    
    for i in range(len(regras[personagem])):
        y = regras[personagem][i]
        if math.cos(y[4]) != 0 and y[1] + math.cos(y[4]) < (SCREEN_WIDTH - 15 -personagem.get_width()) and y[1] + math.cos(y[4]) > 15 and nocoli(personagem, y[0] % 10 ,[y[1] + math.cos(y[4]) * 3, y[2]]):
            regras[personagem][i] = [y[0], y[1] + math.cos(y[4]) * 3, y[2], y[3], y[4], y[5], y[6]]
        
        y = regras[personagem][i]
    
        if y[2] - math.sin(y[4]) > 13 and y[2] - math.sin(y[4]) < SCREEN_HEIGHT - 57 - personagem.get_height() and math.sin(y[4]) != 0 and nocoli(personagem, y[0] % 10 ,[y[1], y[2] - math.sin(y[4]) * 3]):
            regras[personagem][i] = [y[0], y[1], y[2] - math.sin(y[4]) * 3, y[3], y[4], y[5], y[6]]
        
    remo = set()
    for i in range(len(regras[flecha])):
        y = regras[flecha][i]
        if math.cos(y[3]) != 0 and y[1] + math.cos(y[3]) < (SCREEN_WIDTH - 15 - flecha.get_width()) and y[1] + math.cos(y[3]) > 15 and nocoli(flecha, y[0] % 10, ( y[1] + math.cos(y[3]) * 10 , y[2])):
            regras[flecha][i] = [y[0], y[1] + math.cos(y[3]) * 10, y[2], y[3]]
        else:
            remo.add(i)
        
        y = regras[flecha][i]
    
        if y[2] - math.sin(y[3]) > 13 and y[2] - math.sin(y[3]) < SCREEN_HEIGHT - 75 - flecha.get_height() and math.sin(y[3]) != 0 and nocoli(flecha, y[0] % 10, ( y[1], y[2] - math.sin(y[3]) * 10)):
            regras[flecha][i] = [y[0], y[1], y[2] - math.sin(y[3]) * 10, y[3]]
        else:
            remo.add(i)
            
    remo = sorted(remo, key = lambda x: -x)
    
    for i in remo:
        remotem.append([copy.deepcopy(regras[flecha][i]), 100])
        regras[flecha].pop(i)
        


    
    #desenhar

    screen_info = pygame.display.Info()
    #fundo = pygame.transform.scale(fundo, (screen_info.current_w, screen_info.current_h))
    #bordas = pygame.transform.scale(bordas, (screen_info.current_w, screen_info.current_h))    
    
    #obstaculo = pygame.transform.scale(obstaculo, (int(obstaculo.get_width() * (kk / screen_info.current_w)) , int(obstaculo.get_height() * (kk2 / screen_info.current_h))))
    
    screen.blit(fundo, (0,0))

    #screen.blit(pedras, (pobx, poby))

    tictac += 1
    if tictac % 1000 == 0 and len(regras[poder]) <= 0:
        bug = False
        while bug == False:
            x1 = random.randrange(50, SCREEN_WIDTH - 50)
            y1 = random.randrange(50, SCREEN_HEIGHT - 100)
            bug = nocoli(poder, x1, y1)
            
        regras[poder].append([2, x1, y1, -1])
        cooldown[poder] = 100
    
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
                    
                    
    screen.blit(bordas, (0,0))
        
    for i in regras[flecha]:
        (cond, x3, y3, ang) = i

        screen.blit(pygame.transform.rotate(flecha, ang / math.pi * 180), (x3, y3))

    for i in range(len(remotem)):
        if remotem[i][1] == 0:
            remotem.pop(i)
            break
        else:
            remotem[i][1] -= 1
            print(remotem[i][0], remotem[i])
            (cond, x3, y3, ang) = remotem[i][0]
            screen.blit(pygame.transform.rotate(flecha, ang / math.pi * 180), (x3, y3))
            
    for i in regras:
        for ii in regras[i]:
            if i == personagem:
                (cond, x3, y3, temp, ang, arma, escd) = ii
                np = cond % 10

                if True:
                    
                    if cooldown[np] <= 0:
                        regras[personagem][np][0] = 40 + np
                        rot_image = roda(personagem, ang)
                        screen.blit(rot_image, (x3, y3))
                    if (cooldown[np] in range (180, 160, -1)) or (cooldown[np] in range(120,80, -1)) or (cooldown[np] in range(40,20, -1)):
                        rot_image = roda(personagemred, ang)
                        screen.blit(rot_image, (x3, y3))
                    
                    #para a arma
                    rot_image = roda(espada, ang)
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
                    rot_image = roda(broca, ang)
                    
                    #para a brocacores
                    rot_image1 = roda(brocacores, ang)
                    
                    if arma == 2:
                        if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:
                            screen.blit(rot_image1, (x3, y3))
                        else:
                            screen.blit(rot_image, (x3, y3))
                    
                    #para o arco
                    rot_image = roda(arco, ang)
                    if arma == 3:
                        screen.blit(rot_image, (x3, y3))
                    
                    #para o escudo
                    rot_image = roda(escudo1, ang)
                    if escd == True:
                        screen.blit(rot_image, (x3, y3))
                    
                
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
                    ii[3] = -1
    cooldown[0] -= (1 if cooldown[0] != 0 else 0)
    cooldown[1] -= (1 if cooldown[1] != 0 else 0)
    
    screen.blit(imavida[vida[0]], (0,0)) if vida[0] > 0 else screen.blit(imavida[0], (0,0))
    screen.blit(imavida[vida[1]], (510,0)) if vida[1] > 0 else screen.blit(imavida[0], (510,0))
        

    #kk = screen_info.current_w
    #kk2 = screen_info.current_h
    pygame.display.flip()
    clock.tick(0)
    
pygame.quit()
