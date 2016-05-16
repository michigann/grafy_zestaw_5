#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Graph import Graph
import sys


vertices = int(sys.argv[1])
if vertices < 2:
	sys.exit("Ilość warstw >= 2!")

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

g.draw()
