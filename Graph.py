#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygraphviz as nx
import matplotlib.pyplot as plt

from random import randint

class Graph:
	def __init__(self, n_layers):
		self.n_layers = n_layers
		self.layers, self.vertices = self.makeLayers()
		self.matrix = self.makeMatrix()

	#tworzy warstwy wraz z losowa liczba wierzcholkow
	#zwraca (liste_warstw, ilosc_wierzcholkow)
	def makeLayers(self):
		layers = []
		layers.append([0])
		next = 1
		for i in range(self.n_layers):
			tmp = []
			for j in range(randint(2, self.n_layers)):
				tmp.append(next)
				next+=1
			layers.append(tmp)
		layers.append([next])
		return layers, next+1
		
	#tworzy macierz przepustowosci sieci
	def makeMatrix(self):
		matrix = [ [0 for i in range(self.vertices)] for j in range(self.vertices)]
		#laczenie wszystkich wierzcholkow warstwy i z warstwa i+1
		for i in range(1, self.n_layers):
			linked_k = []
			#laczenie wszystkich wierzcholkow warstwy i
			for j in self.layers[i]:
				rand_k = randint(self.layers[i+1][0], self.layers[i+1][-1])
				if len(linked_k) != len(self.layers[i+1]):
					while rand_k in linked_k:
						rand_k = randint(self.layers[i+1][0], self.layers[i+1][-1])
					linked_k.append(rand_k)	
				matrix[j][rand_k] = 1

			#laczenie pozostalych wierzcholkow warstwy i+1
			if len(linked_k) != len(self.layers[i+1]):
				for k in self.layers[i+1]:
					if k not in linked_k:
						linked_k.append(k)
						rand_j = randint(self.layers[i][0], self.layers[i][-1])
						matrix[rand_j][k] = 1


		#laczenie zrodla i ujscia		
		for i in self.layers[1]:
			matrix[0][i] = 1
		for i in self.layers[-2]:
			matrix[i][-1] = 1

		#dodawanie 2*N losowych krawedzi
		for i in range(self.n_layers*2):
			v1, v2 = None, None
			while True:
				v1 = randint(2, self.layers[-2][-1])
				v2 = randint(2, self.layers[-2][-1])
				while v1==v2:
					v2 = randint(2, self.layers[-2][-1])
				if matrix[v1][v2] == 0:
					matrix[v1][v2] = 1
				elif matrix[v2][v1] == 0:
					matrix[v2][v1] = 1
				else:
					continue
				break

		#dodawanie przepustowosci
		for i in range(self.vertices):
			for j in range(self.vertices):
				if matrix[i][j]==1:
					matrix[i][j]=randint(1, 9)
					
		return matrix

