#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Graph import Graph
from random import randint

import pygraphviz as nx
import matplotlib.pyplot as plt

class Bipartite(Graph):
	def __init__(self):
		self.n_layers = 2
		self.layers, self.vertices = self.makeLayers()
		self.matrix = self.makeMatrix()
	
	def makeLayers(self):
		layers = []
		layers.append([0])
		next = 1
		num = randint(2,5)
		#if num%2==1:
		#	num+=1
		for i in range(2):
			tmp = []
			for j in range(num):
				tmp.append(next)
				next+=1
			layers.append(tmp)
		layers.append([next])
		return layers, next+1
		
	def makeMatrix(self):
		matrix = [ [0 for i in range(self.vertices)] for j in range(self.vertices)]
		#laczenie wszystkich wierzcholkow warstwy i z warstwa i+1
		linked_k = []
		for j in self.layers[1]:
			rand_k = randint(self.layers[2][0], self.layers[2][-1])
			#while rand_k in linked_k:
			#	rand_k = randint(self.layers[2][0], self.layers[2][-1])
			linked_k.append(rand_k)
			matrix[j][rand_k] = 1 
		
		for j in self.layers[2]:
			if j not in linked_k:
				tmp = randint(self.layers[1][0], self.layers[1][-1])
				matrix[tmp][j] = 1  

		#laczenie zrodla i ujscia		
		for i in self.layers[1]:
			matrix[0][i] = 1
		for i in self.layers[2]:
			matrix[i][-1] = 1

		#dodawanie 2*N losowych krawedzi
		for i in range(4):
			v1, v2 = None, None
			tmp=0
			while tmp<200:
				v1 = randint(2, self.layers[1][-1])
				v2 = randint(self.layers[2][0], self.layers[2][-1])
				if matrix[v1][v2] == 0:
					matrix[v1][v2] = 1
				else:
					tmp+=1
					continue
				break
					
		return matrix
	
	
	
	def show(self):
		for i in self.matrix:
			print(i)
	
	def showLinked(self):
		for i in self.matrix:
			for j in i:
				if matrix[i][j]==1:
					print(str(i)+" -> "+str(j))
	
	
		
	
