#If we make the array sorted the time complexity will be O(n)

fdata = open('input1.txt')

fdata= fdata.read()

file = open('output1.txt', 'w')

data = fdata.split('\n')

length = data[0]

arr = data[1]

arr = arr.split(" ")

def bubbleSort(arr):
    arr = sorted(arr)
    for i in range(len(arr)-1):
        check = 0
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                check = 1
        if (check != 1):
            break

    for i in arr:
    
        file.write(i + " ")

bubbleSort(arr)

    