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

for i in g.layers:
	print(i)
	
	
counter = 0
#print(g.vertices)
for i in g.matrix:
	print(i)
	for j in i:
		if j>0:
			counter+=1
print(counter)

maxFlow = MaxFlow(g)
print(maxFlow.max_flow())

for i in maxFlow.flowMatrix:
	print(i)

bipartite = Bipartite() 
bipartiteMaxFlow = MaxFlow(bipartite)
print(bipartiteMaxFlow.max_flow())
bipartite.show()
print('''
''')
bipartiteMaxFlow.show()


raw_input('Enter to draw a graph...')
draw(g, maxFlow)
#draw(bipartite, bipartiteMaxFlow)
