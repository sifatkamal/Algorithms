fdata = open('input.txt')

fdata= fdata.read()

file = open('output.txt', 'w')

data = fdata.split('\n')

graph = {}

index = 1

for i in range(len(data)-1):
    
    value = " ".join(data[index].split())
    
    value = value.split(" ")
    
    print(value)
    
    key = value.pop(0)
    
    graph[key] = value
    
    index+=1
    
#print(graph)    

visited = []

queue = []

def BFS(visited, graph, node, endPoint):
    
    visited.append(node)
    
    queue.append(node)

    while queue:
  
        s = queue.pop(0)
        
        if s == endPoint:
            
            file.write(s + " ")
            
            break
        
        else:
            
            file.write(s + " ")
            
            for i in graph[s]:
            
                if i not in visited:
                  
                    visited.append(i)
                    
                    queue.append(i)

BFS(visited, graph, '1', '12')