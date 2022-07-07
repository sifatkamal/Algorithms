fdata = open('input3.txt')

fdata= fdata.read()

file = open('output3.txt', 'w')

data = fdata.split('\n')

length = data[0]

length = int(length)

ID = data[1]

arr = data[2]

ID = ID.split(" ")

arr = arr.split(" ")

arr = [int(item) for item in arr]

ID = [int(item) for item in ID]

#=========================================================

def insertionSort(arr, ID):
    
    count = 0
    
    index = 0

    for i in range(length):
 
        value = arr[i]
        
        value_1 = ID[i]
 
        count = i - 1
 
        while (count >= 0) and (value > arr[count]):
            
            arr[count + 1] = arr[count]
            
            ID[count +1 ] = ID[count]
 
            count -= 1

        arr[count + 1] = value
        
        ID[count + 1] = value_1
        
    ID = [str(item) for item in ID]
    
    for i in range(length):
    
        file.write(ID[index] + " ")
        
        index+=1

    
    

insertionSort(arr, ID)