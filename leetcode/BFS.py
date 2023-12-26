graph = {
	'A' : ['B', 'G'],
	'B' : ['C', 'D', 'E'],
	'C' : [],
	'D' : [],
	'E' : ['F'],
	'F' : [],
	'G' : ['H'],
	'H' : ['I'],
	'I' : [],
}

def bfs(graph, node):
	visited = []
	queue = []
	
	visited.append(node)
	queue.append(node)
	
	while(queue):
		s = queue.pop(0)
		print(s, end = " ")
		
		for n in graph[s]:
			if n not in visited:
				visited.append(n)
				queue.append(n)

print(bfs(graph, 'A'))
