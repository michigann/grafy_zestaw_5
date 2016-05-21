from Graph import Graph
from random import randint

class MaxFlow:
	def __init__(self, graph):
		self.graph = graph
		self.flowMatrix = [ [0 for i in range(graph.vertices)] for j in range(graph.vertices)]
		self.Al=[[] for i in range(graph.vertices)]
		for i in range(graph.vertices):
			for j in range(graph.vertices):
				if graph.matrix[i][j]>0:
					self.Al[i].append(j)
		
	def find_path(self, source, end, path=[]):
		if(source == end):
			return path
		for i in self.Al[source]:
			if (self.graph.matrix[source][i]-self.flowMatrix[source][i])>0 and i not in path:
				p = self.find_path(i,end,path+[i])
				if p!=None:
					return p
	def show(self):
		for i in self.flowMatrix:
			print(i)
			
	def max_flow(self):
		path = self.find_path(0,self.graph.vertices-1,[])
		while(path != None):
			temp = []
			temp.append(self.graph.matrix[0][path[0]]-self.flowMatrix[0][path[0]])
			for i in range(len(path)-1):
				temp.append(self.graph.matrix[path[i]][path[i+1]]-self.flowMatrix[path[i]][path[i+1]])
			flow = min(temp)
			self.flowMatrix[0][path[0]]+=flow
			for i in range(len(path)-1):
				self.flowMatrix[path[i]][path[i+1]]+=flow
			path = self.find_path(0,self.graph.vertices-1,[])
		return sum(self.flowMatrix[0][i] for i in self.Al[0])
