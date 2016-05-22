#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, pygame
import pygame.gfxdraw
from random import randint
from Graph import Graph
from Bipartite import Bipartite


def index_2d(my_list, v):
    # pobranie indexu wartości v z listy 2d
    for i, x in enumerate(my_list):
        if v in x:
            return i, x.index(v)

def init_coordinates(width, height, n_layers, layers, v_in_layer):
    # inicjalizacja współrzędnych kolejnych wierzchołków
    r = 30
    step = (width)/(v_in_layer+1), height/v_in_layer+20
    coords = []
    coords.append([(20, height/2)])
    for i in range(1, n_layers+1):
        n = len(layers[i])
        y = height / 2
        if n%2 == 0:
            y = height / 2 + step[1]/2
        for j in range(n/2+1):
            y-=step[1]
        coords.append( [(step[0]*i+randint(-r, r), y+step[1]*j+randint(-r,r)) for j in range(1, n+1)] )
    coords.append([(width-20, height/2)])
    return coords

def draw_line(screen, color, k, l):
    # rysowanie strzałki z pkt. k do l
    pygame.draw.line(screen, color, k, l)
    v = (l[0] - k[0]) / 4, (l[1] - k[1]) / 4
    k = l[0] - v[0], l[1] - v[1]
    pygame.draw.line(screen, color, k, l, 4)

def draw_flow(screen, text, k, l, flag=True):
    #rysuje przeplyw miedzy k i l
    v = (l[0] - k[0]) / 2, (l[1] - k[1]) / 2
    k = [k[0] + v[0], k[1] + v[1]]
    if flag:
        k[1]-=10
    else:
        k[1]+=10
    screen.blit(text, k)


def draw(g, maxFlow):
    # rysowanie grafu z przeplywami
    # g - obiekt Graph

    n_layers = g.n_layers
    v_in_layer = n_layers
    if isinstance(g, Bipartite):
    	v_in_layer = (g.vertices-2)/2
    layers = g.layers
    matrix = g.matrix
    vertices = g.vertices

    flowMatrix = maxFlow.flowMatrix

    size = width, height = 1024, 768
    black, white, red, green, blue = (0,0,0), (255,255,255), (255,0,0), (0,255,0), (0,0,255)
    radius = 15

    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill(white)

	
    coords = init_coordinates(width, height, n_layers, layers, v_in_layer)

    font = pygame.font.SysFont("Arial", 12)



    for i in range(vertices):
        for j in range(i+1, vertices):
            if matrix[i][j] != 0 or matrix[j][i] != 0:
            	x, y = i, j
                color = green
                k, l = index_2d(layers, i), index_2d(layers, j)
                k, l = coords[k[0]][k[1]], coords[l[0]][l[1]]
                if matrix[i][j] != 0 and matrix[j][i] != 0:
                    k, l = (k[0] - radius/2, k[1] - radius/2), (l[0] - radius / 2, l[1] - radius / 2)
                    draw_line(screen, color, k, l)
                    draw_flow(screen, font.render(str(matrix[i][j]) + "/" + str(flowMatrix[i][j]), True, black), k, l)
                    k, l = (k[0] + radius, k[1] + radius), (l[0] + radius, l[1] + radius)
                    draw_line(screen, red, l, k)
                    draw_flow(screen, font.render(str(matrix[j][i]) + "/" + str(flowMatrix[j][i]), True, black), k, l, False)
                    continue
                elif matrix[j][i] != 0:
                	x, y = y, x
                	k, l = l, k
                	color = red

                draw_line(screen, color, k, l)
                draw_flow(screen, font.render(str(matrix[x][y]) + "/" + str(flowMatrix[x][y]), True, black), k, l)

    v_counter = 0
    font = pygame.font.SysFont("Arial", 18, bold=True)
    for i in coords:
        for j in i:
            pygame.draw.circle(screen, black, j, radius)
            text = font.render(str(v_counter), True, white)
            if v_counter < 10:
                pos = j[0]-radius/2+2, j[1]-radius+4
            else:
                pos = j[0] - radius+4, j[1]-radius+4
            screen.blit(text, pos)
            v_counter+=1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            	return
                #pygame.display.quit()
                #pygame.quit()
                #sys.exit()
        pygame.display.update()
        pygame.time.delay(100)
