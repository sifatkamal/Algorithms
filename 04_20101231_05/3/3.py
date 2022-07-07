fdata = open('input.txt')

fdata= fdata.read()

file = open('output.txt', 'w')

data = fdata.split('\n')

n = int(data.pop(0))

for i in data:
    
    listt = data[0].split(" ")
    
    command = data[1]
    
for i in range(n):
    
    listt[i] = int(listt[i])    

def Assignment_Selection(listt, n):
    
    listt.sort()
    
    queue = []

    Jack = 0
    
    Jill = 0

    index = 0
    
    sequence = []
            
    for c in command:
        
        if c == "J":
            
            value_1 = listt[index]
            
            queue.append(listt[index])
            
            sequence.append(listt[index])
            
            Jack = value_1 + Jack
            
            index+=1
            
        elif c == "j":
            
            store = queue.pop(-1)
            
            value_2 = store
            
            sequence.append(store)
            
            Jill = value_2 + Jill
    
    count = 0
    
    for i in sequence:
        
        file.write(str(sequence[count]))
        
        count+=1
        
    file.write("\n")    

    file.write("Jack will work for " + str(Jack) + " hours" + "\n")

    file.write("Jill will work for " + str(Jill) + " hours")        

Assignment_Selection(listt, n)






