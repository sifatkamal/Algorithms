fdata = open('input.txt')

fdata= fdata.read()

file = open('output.txt', 'w')

data = fdata.split('\n')

first = data.pop(0)

a, n = first.split(" ")

a, n = int(a), int(n)

index = 0

listt = []

for i in data:
    
    store = data[index].split(" ")
    
    for i in range(len(store)):
        
        store[i] = int(store[i])
    
    listt.append(store)
    
    index+=1

def Assignment_Selection(listt, n, a):

    listt_2 = []
    
    for unknown in range(n):
    	
        for i in range(a):
    	    
            for j in range(0, a-i-1):
                
                if (listt[j][1] > listt[j + 1][1]):
                    
                    store = listt[j]
                    
                    listt[j]= listt[j + 1]
                    
                    listt[j + 1]= store
                    
        count = 0
        
        listt_2.append(listt[count])
    
        for i in range(a):
            
            if listt[i][0] >= listt[count][1]:
                
                listt_2.append(listt[i])
                
                count = i
        
        if listt != []:
            
            for i in listt:
                
                for j in listt_2:
                    
                    if j == i:
                        
                        listt.remove(i)
                        
        a = len(listt)                
        
    size = len(listt_2)
        
    print(size)
    
    file.write(str(size) + '\n')

Assignment_Selection(listt, n, a)