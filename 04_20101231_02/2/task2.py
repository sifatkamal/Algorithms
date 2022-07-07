fdata = open('input2.txt')

fdata= fdata.read()

file = open('output2.txt', 'w')

data = fdata.split('\n')

first = data[0]

M, N = first.split(" ")

M = int(M)

N = int(N)

arr = data[1]

arr = arr.split(" ")

arr = [int(item) for item in arr]

def insertionSort(arr):
    
    index = 0
    
    count = 0

    for i in range(M):
 
        value = arr[i]
 
        count = i - 1
 
        while (count >= 0) and (value < arr[count]):
            
            arr[count + 1] = arr[count]
 
            count -= 1

        arr[count + 1] = value
        
    arr = [str(item) for item in arr]    
        
    for i in range(N):
        
        file.write(arr[index] + " ")
        
        index+=1



insertionSort(arr)
