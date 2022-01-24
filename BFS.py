graph = {
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','C','E','F'],
    'E':['C','D'],
    'F':['D']
}

def BFS(graph,node):
    queue = []
    col = set()
    queue.append(node)
    col.add(node)
    while(len(queue)>0):
        vertex = queue.pop(0)
        for i in graph[vertex]:
            if i not in col:
                queue.append(i)
                col.add(i)
        print(vertex)

BFS(graph,'A')

