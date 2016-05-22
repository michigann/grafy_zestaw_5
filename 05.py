#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
pygame install
sudo apt-get install python-pygame
'''

from Graph import Graph
from Draw import draw
from Bipartite import Bipartite
from MaxFlow import MaxFlow
import sys



vertices = int(sys.argv[1])
if vertices < 2:
	sys.exit("Min layers >= 2!")

g = Graph(vertices)

print("\nPodział grafu na poszczególne warstwy:")
for i in g.layers:
	print(i)
	
	
counter = 0
print("\nMacierz sąsiedztwa:")
for i in g.matrix:
	print(i)
	for j in i:
		if j>0:
			counter+=1

maxFlow = MaxFlow(g)
print("\nMaksymalny przepływ = "+str(maxFlow.max_flow()))
print("\nMacierz przepływów:")
for i in maxFlow.flowMatrix:
	print(i)
	
draw(g, maxFlow)

bipartite = Bipartite() 
bipartiteMaxFlow = MaxFlow(bipartite)

print("\nGraf dwudzielny:")
bipartite.show()

print("\nMaksymalny przepływ na grafie dwudzielnym = "+str(bipartiteMaxFlow.max_flow()))
print("\nMacierz przepływów na grafie dwudzielnym:")
bipartiteMaxFlow.show()

print("\nPołączone pary:")
temp = bipartiteMaxFlow.flowMatrix
for i in range(1,len(temp)-1):
	for j in range(1,len(temp)-1):
		if temp[i][j]==1:
			print(str(i)+" -> "+str(j))

draw(bipartite, bipartiteMaxFlow)
