fdata = open('input.txt')

fdata= fdata.read()

file = open('output.txt', 'w')

data = fdata.split('\n')

graph = {}

index = 1

for i in range(len(data)-1):
    
    value = " ".join(data[index].split())
    
    value = value.split(" ")
    
    key = value.pop(0)
    
    graph[key] = value
    
    index+=1   

visited = set()

listt = []

def DFS(visited, graph, node):
    
    if node not in visited:
        
        listt.append(node)
        
        visited.add(node)
        
        for i in graph[node]:
        
            DFS(visited, graph, i)
            
    return listt       
                
DFS(visited, graph, '1')

for i in listt:
    
    if i == "12":
        
        file.write(i + " ")
        
        break
    
    else:
        
        file.write(i + " ")