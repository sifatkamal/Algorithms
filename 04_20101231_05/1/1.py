fdata = open('input.txt')

fdata= fdata.read()

file = open('output.txt', 'w')

data = fdata.split('\n')

n = int(data.pop(0))

listt = []

index = 0

for i in data:
    
    store = data[index].split(" ")
    
    for i in range(len(store)):
        
        store[i] = int(store[i])
    
    listt.append(store)
    
    index+=1

        

def Assignment_Selection(listt, n):

    listt_2 = []
	
    for i in range(n):
	    
        for j in range(0, n-i-1):
            
            if (listt[j][1] > listt[j + 1][1]):
                
                store = listt[j]
                
                listt[j]= listt[j + 1]
                
                listt[j + 1]= store	
                
    count = 0
    
    listt_2.append(listt[count])

    for i in range(n):
        
        if listt[i][0] >= listt[count][1]:
            
            listt_2.append(listt[i])
            
            count = i
	
    size = len(listt_2)
    
    print(size)
    
    file.write(str(size) + '\n')
    
    for i in listt_2:
	    
        index = 0
        
        file.write(str(i[index]) +" ")
        
        print(i[index], end = " ")
        
        index+=1
        
        print(i[index])
        
        file.write(str(i[index]) + '\n')

Assignment_Selection(listt, n)
