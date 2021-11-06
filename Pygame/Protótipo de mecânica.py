#PROTÓTIPO DE MECÂNICA DO JOGO (em pygthon)

#IMPORTAÇÃO DE BIBLIOTECAS
import pygame as py #Biblioteca utilizada para a criação de jogos em python
import math #Biblioteca utilizada para maiores cálculos matemáticos
from random import randint
import time
#---------------------x----------------------

#ABERTURA DA TELA
py.init()
tela = py.display.set_mode((640,540))
telaaberta = True

#---------------------x----------------------

#NOME, IMPORTAÇÃO DA TELA E DO FUNDO DE JOGO
py.display.set_caption('Protótipo de mecânica') #Define o nome do jogo
spr_fundo = py.image.load('fundoPI.png') #Importando a imagem de fundo
spr_icone = py.image.load('logo3.png') #Importando a imagem do ícone
py.display.set_icon(spr_icone) #Define o ícone

#---------------------x----------------------

#CONFIGURAÇÕES DO PLAYER
spr_player = py.image.load('playeridle1.png') #Importando o sprite do player
playerX = 320
playerY = 240
player_velocidadeX = 0
player_velocidadeY = 0
def player(x, y): #Está sempre "redesenhando" o player de acordo com a coordenada recebida
    tela.blit(spr_player, (x, y))

#---------------------x----------------------

#LATA
spr_lata = py.image.load('lata.png') #importando a imagem lata
lataX = randint(60, 600)
lataY = randint(40, 400)

def lata(x, y):
    tela.blit(spr_lata, (x, y))

#---------------------x----------------------

#PONTUAÇÃO
pontuacao_valor = 10
fonte = py.font.Font('freesansbold.ttf', 25) #Configurações/parâmetros na fonte da pontuação
textoX = 85
textoY = 490
def mostrar_valor(x, y):
    pontuacao = fonte.render('Colete 10 latas espalhadas pelo chão.', True, (255, 255, 255))
    tela.blit(pontuacao, (x, y))

#---------------------x----------------------

#COLISÃO (ENTRE A LATA E O PLAYER)
def estacolidindo(lataX, lataY, playerX, playerY):
    distancia = math.sqrt(math.pow(lataX - playerX, 2) + (math.pow(lataY - playerY, 2))) #Equação que irá calcular a distancia de um objeto para o outro
    if distancia < 100: #Se a distancia for menor que 10 pixels retorna-se true, se não, falso
        return True
    else:
        return False

#---------------------x----------------------

#DEFININDO LOOP DE EVENTOS GLOBAIS
while telaaberta:
    if pontuacao_valor <= 0:
        time.sleep(3)
        tela = py.WINDOWCLOSE #Fecha a tela após serem coletadas 10 latas
    tela.blit(spr_fundo,(0, 0)) #"Desenha" a imagem de fundo em uma certa posição
    for event in py.event.get():
        if event.type == py.QUIT: #Evento chamado quando fecha a tela
            telaaberta = False #Define a tela como false, sendo fechada logo em seguida

#---------------------x----------------------

#MOVIMENTAÇÃO DO PLAYER (baseada em eventos que captam se a tecla foi pressionada, caso for, ocorre uma ação.)
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                player_velocidadeX = -3
            if event.key == py.K_RIGHT:
                player_velocidadeX = 3
            if event.key == py.K_UP:
                player_velocidadeY = -3
            if event.key == py.K_DOWN:
                player_velocidadeY = 3
        if event.type == py.KEYUP:
            if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                pressionado = py.key.get_pressed()
                if not pressionado[py.K_LEFT] and not pressionado[py.K_RIGHT]:
                    player_velocidadeX = 0

            if event.key == py.K_UP or event.key == py.K_DOWN:
                pressionado = py.key.get_pressed()
                if not pressionado[py.K_UP] and not pressionado[py.K_DOWN]:
                    player_velocidadeY = 0

    playerX += player_velocidadeX  # Soma a velocidade + a posição X do player
    playerY += player_velocidadeY  # Soma a velocidade + a posição Y do player

#---------------------x----------------------

#DEFININDO LIMITE MÁXIMO DO MAPA (área de gameplay)
    if playerX <= 0:
        playerX = 0
    elif playerX >= 570:
        playerX = 570
    if playerY <= 0:
        playerY = 0
    elif playerY >= 410:
        playerY = 410

#---------------------x----------------------

#COLISÃO + ATUALIZAÇÃO DE TEXTO
    colisao = estacolidindo(lataX, lataY, playerX, playerY) #Define "colisao" como um evento que ocorre em dadas coordenadas X e Y
    if colisao:
        pontuacao_valor -= 1
        lataX = randint(60, 600)
        lataY = randint(40, 400)

#---------------------x----------------------

#VISUALIZAÇÃO DE ELEMENTOS
    mostrar_valor(textoX, textoY) #Mostra o valor/texto na tela
    lata(lataX, lataY) #Define a posição da lata baseado nos pontos X e Y
    player(playerX, playerY) #Sempre enviando as coordenadas atuais do player
    py.display.update() #Sempre irá atualizar as informações que ocorrem na tela