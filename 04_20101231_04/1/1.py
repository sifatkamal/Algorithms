import sys

fdata = open('input.txt')

fdata= fdata.read()

file = open('output.txt', 'w')

data = fdata.split('\n')

limit = int(data.pop(0))

def Dijkstra(matrixx, source):
        
    index = 0
    
    dist = [[0, 0]]
    
    for i in range(vertex - 1):
        
        dist.append([0, sys.maxsize])
    
    for i in range(vertex):
        
        v = -10
    
        for index in range(vertex):
    
            if (dist[index][0] == 0) and (v < 0 or dist[index][1] <= dist[v][1]):
                
                v = index
    
        for i in range(vertex):
    
            if (matrixx[v][i] == 1) and (dist[i][0]) == 0:
                
                distance_2 = dist[v][1] + edges[v][i]
                
                if (dist[i][1] > distance_2):
                
                    dist[i][1] = distance_2
            
            dist[v][0] = 1
    
    store = []
    
    for i in dist:
        
        store.append(i[1])
        
    file.write(str(max(store)) + "\n")    
        
    return max(store)
    
index = 0

for i in range(limit):
    
    listt = []
    
    vertex, edge = data[index].split(" ")
    
    vertex = int(vertex)
    
    edge = int(edge)
    
    if (vertex == 1):
        
        print(edge)
        
        file.write(str(edge) + "\n")
        
        data.pop(index)
        
        continue
        
    else:    
    
        data.pop(index)
        
        index_2 = 0
        
        for j in range(int(edge)):
            
            listt.append(data[index_2])
            
            data.pop(index_2)
            
        index_2 = 0
        
        double = vertex * vertex
        
        graph = [0] * double
        
        row_count = vertex
        
        col_count = row_count
        
        matrixx = []
        
        edges = []
        
        for i in range(row_count):
        
            row_list = []
        
            for j in range(col_count):
        
                row_list.append(graph[row_count * i + j])
        
            matrixx.append(row_list)
        
        for j in range(row_count):
        
            row_list = []
        
            for j in range(col_count):
        
                row_list.append(graph[row_count * i + j])
        
            edges.append(row_list)
        
        value = 0
        
        for j in range(len(listt)):
            
            node_1, node_2, weight = listt[value].split(" ")
            
            node_1 = int(node_1)
            
            node_2 = int(node_2)
            
            weight = int(weight)
            
            value+=1
            
            count_1 = 1
            
            count_2 = 1
                        
            for i in matrixx:
                
                if count_1 == int(node_1):
                    
                    i[node_2 - 1] = 1
                
                count_1+=1
                
            for i in edges:
                
                if count_2 == int(node_1):
                    
                    i[node_2-1] = weight
                
                count_2+=1

            source = 1
    
    print(Dijkstra(matrixx, source))
    
    