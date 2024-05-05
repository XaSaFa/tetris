import random
import numpy as np
import pygame
from pygame.locals import *

# El tablero tiene 22 posiciones de alto, 2 fuera del tablero de juego propiamente dicho y 20 efectivas.
ALTO = 22
ANCHO = 10
pantalla_ancho = 640
pantalla_alto = 480
ALPHA = 100
COLOR_TRANSPARENTE = (0,0,0,ALPHA)
temps_jugada = 400
temps_ultima_jugada = 0
tiempo_accion = 100
tiempo_ultima_accion = 0
puntos = 0


tablero = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
            ]
vista = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
            ]
temporal = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
            ]
pieza = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
            ]

figuras = [[[3, 3, 3, 3], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[2, 2, 2], [0, 2, 0], [0, 0, 0]],
           [[1, 1, 0], [0, 1, 1], [0, 0, 0]], [[0, 4, 4], [4, 4, 0], [0, 0, 0]],
           [[5, 5, 5], [0, 0, 5], [0, 0, 0]], [[6, 6, 6], [6, 0, 0], [0, 0, 0]], [[7, 7], [7, 7]]]

pygame.init()
pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))
# CREAR LA SUPERFÍCIE TRANSPARENTE I EL RECTÁNGULO SOBRE ELLA:
seccion_transparente = pygame.Surface((200,400),pygame.SRCALPHA)
pygame.draw.rect(seccion_transparente,COLOR_TRANSPARENTE,(0,0,200,400))
# Imágenes
BACKGROUND_IMAGE = 'assets/mar.png'
green_tile = pygame.image.load('assets/green-tile.png').convert()
orange_tile = pygame.image.load('assets/orange-tile.png').convert()
red_tile = pygame.image.load('assets/red-tile.png').convert()
yellow_tile = pygame.image.load('assets/yellow-tile.png').convert()
purple_tile = pygame.image.load('assets/purple-tile.png').convert()
blue_tile = pygame.image.load('assets/blue-tile.png').convert()
pink_tile = pygame.image.load('assets/pink-tile.png').convert()

# Control de FPS
clock = pygame.time.Clock()
fps = 30

# Imprimir una imagen de fondo:
def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

# Esta función deja a cero la matriz pieza
def vaciar_pieza():
    pieza = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
            ]
    return pieza

# Esta función saca una pieza al azar entre las 7 posibles
def elegir_pieza():
    pieza = vaciar_pieza()
    x = 4
    y1 = 0
    num = random.randint(0,6)
    figura1 = figuras[num]
    for i in figura1:
        x1 = x
        for j in i:
            pieza[y1][x1] = j
            x1 += 1
        y1 += 1
    return pieza


# Copia matriz origen a matriz destino
def copia_matriz(matriz_origen,matriz_destino):
    for a in range(0, ALTO):
        for b in range(0, ANCHO):
            matriz_destino[a][b] = matriz_origen[a][b]

# Copia las posiciones que no son cero entre dos matrices, así la matriz vista tiene
# en ella las piezas que están ya fijas en el tablero y la pieza que va bajando
def crear_vista(vista, tablero, pieza):
    for a in range(0, ALTO):
        for b in range(0, ANCHO):
            vista[a][b] = tablero[a][b]
            if pieza[a][b]>0:
                vista[a][b]=pieza[a][b]
    return vista

# Esta función comprueba si la pieza que está bajando se ha quedado arriba por lo que el tablero está lleno
def comprobar_arriba():
    arriba = False
    for a in range(0, 1):
        for b in range(0, ANCHO):
            if pieza[a][b] * tablero[a][b] > 0:
                arriba = True
    return arriba

# Esta función imprime en el tablero los rectángulos del color que tengan en su posición
def imprimir_piezas():
    for fila in range(0,ALTO):
        for pos in range(0,ANCHO):
            if vista[fila][pos] > 0:
                x = pos * 20
                y = fila * 20
                if vista[fila][pos] == 1:
                    pantalla.blit(green_tile, ( 100 + x,  y))
                elif vista[fila][pos] == 2:
                    pantalla.blit(orange_tile, (100 + x, y))
                elif vista[fila][pos] == 3:
                    pantalla.blit(red_tile, (100 + x, y))
                elif vista[fila][pos] == 4:
                    pantalla.blit(purple_tile, (100 + x, y))
                elif vista[fila][pos] == 5:
                    pantalla.blit(yellow_tile, (100 + x, y))
                elif vista[fila][pos] == 6:
                    pantalla.blit(blue_tile, (100 + x, y))
                elif vista[fila][pos] == 7:
                    pantalla.blit(pink_tile, (100 + x, y))





# Esta función baja una fila la pieza
def bajar_pieza():
    pieza.pop()
    pieza.insert(0,[0,0,0,0,0,0,0,0,0,0])


# Esta función comprueba si la pieza colisiona con la parte de abajo del tablero
def comprobar_llega_abajo():
    colisiona = False
    for a in range(0,ANCHO):
        if pieza[ALTO-1][a] > 0:
            colisiona = True

    return colisiona

# esta función comprueba si las matrices que se le envían tienen algún valor no 0 en posiciones iguales
# sirve para saber si hay colisión de piezas entre las dos matrices
def comprobar_colision(matriz1, matriz2):
    colisiona = False
    for a in range(0, ALTO):
        for b in range(0, ANCHO):
            if matriz1[a][b]*matriz2[a][b] > 0:
                colisiona = True
    return colisiona

# Esta función mueve la pieza que baja una posición a la izquierda
def mover_izquierda():
    #comprobar que se no está ya a la izquierda
    puede_mover = True
    for a in range(0, ALTO):
            if pieza[a][0] > 0:
                puede_mover = False
    #si no está a la izquierda movemos la pieza temporal a la izquierda
    copia_matriz(pieza,temporal)
    if puede_mover:
        for a in range(0, ALTO):
            temporal[a].pop(0)
            temporal[a].append(0)
        puede_mover = not comprobar_colision(temporal, tablero)
    return puede_mover

# Esta función mueve la pieza que baja una posición a la derecha
def mover_derecha():
    #comprobar que se no está ya a la derecha
    puede_mover = True
    for a in range(0, ALTO):
            if pieza[a][ANCHO-1] > 0:
                puede_mover = False
    #si no está a la cerecha movemos la pieza temporal a la derecha
    copia_matriz(pieza,temporal)
    if puede_mover:
        for a in range(0, ALTO):
            temporal[a].pop(ANCHO-1)
            temporal[a].insert(0,0)
        puede_mover = not comprobar_colision(temporal, tablero)
    return puede_mover

# Esta función gira 90 grados la pieza que está bajando
def rotar():
    puede_rotar = True
    min_x = ANCHO
    min_y = ALTO
    max_x = 0
    max_y = 0
    for a in range(0, ALTO):
        for b in range(0, ANCHO):
            if pieza[a][b] > 0:
                if a < min_y:
                    min_y = a
                if b < min_x:
                    min_x = b
                if b > max_x:
                    max_x = b
                if a > max_y:
                    max_y = a
    talla_matriz = 3
    if max_x - min_x >=3 or max_y - min_y >= 3:
        talla_matriz = 4
    lista_pieza = []
    for a in range(min_y,min_y+talla_matriz):
        lista_inicial = []
        for b in range(min_x,min_x+talla_matriz):
            lista_inicial.append(pieza[a][b])
        lista_pieza.append(lista_inicial)
    lista_pieza = np.array(lista_pieza)
    lista_pieza = np.rot90(lista_pieza)
    vaciar_pieza()
    copia_matriz(pieza,temporal)
    a1 = 0
    for a in range(min_y,min_y+talla_matriz):
        b1 = 0
        for b in range(min_x,min_x+talla_matriz):
            temporal[a][b] = lista_pieza[a1][b1]
            b1 += 1
        a1 += 1

    return comprobar_colision(temporal,tablero)

# Esta función comprueba si hay alguna línea llena, si es así la quita de tablero, añade una fila arriba y suma un punto por fila
def comprobar_linea_entera():
    puntos = 0
    completas = []
    for a in range(0, ALTO):
        linea = 1
        for b in range(0, ANCHO):
            linea = linea * tablero[a][b]
        if linea > 0:
            completas.append(a)
    for l in completas:
        tablero.pop(l)
        tablero.insert(0,[0,0,0,0,0,0,0,0,0,0])
        puntos += 1
    return puntos

salir = False
pieza = elegir_pieza()

while not (salir):
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if event.type == KEYDOWN and current_time - tiempo_ultima_accion > tiempo_accion:
        if event.key == K_LEFT:
            if mover_izquierda():
                copia_matriz(temporal,pieza)
            tiempo_ultima_accion = current_time

        elif event.key == K_RIGHT:
            if mover_derecha():
                copia_matriz(temporal,pieza)
            tiempo_ultima_accion = current_time
        elif event.key == K_DOWN:
            temps_ultima_jugada -= temps_jugada
        elif event.key == K_UP:
            try:
                if not rotar():
                    copia_matriz(temporal,pieza)
                tiempo_ultima_accion = current_time
            except:
                pass
    vista = crear_vista(vista,tablero,pieza)
    #Imprimir gráficos:
    imprimir_pantalla_fons(BACKGROUND_IMAGE)
    pantalla.blit(seccion_transparente, (100, 40))
    imprimir_piezas()
    pygame.display.update()
    clock.tick(fps)
    current_time = pygame.time.get_ticks()
    if comprobar_llega_abajo():
        copia_matriz(vista, tablero)
        puntos += comprobar_linea_entera()
        pieza = elegir_pieza()
    else:
        if current_time -  temps_ultima_jugada > temps_jugada:
            temps_ultima_jugada = current_time
            bajar_pieza()
            if comprobar_colision(pieza,tablero):
                copia_matriz(vista, tablero)
                puntos += comprobar_linea_entera()
                pieza = elegir_pieza()
    if comprobar_arriba():
        break
    print(puntos)
    if puntos >= 2:
        temps_jugada = 300
    if puntos >= 4:
        temps_jugada = 200
    if puntos >= 6:
        temps_jugada = 100
    if puntos >= 8:
        temps_jugada = 50
    if puntos >= 10:
        temps_jugada = 30



