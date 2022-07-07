fdata = open('input4.txt')

fdata= fdata.read()

file = open('output4.txt', 'w')

data = fdata.split('\n')

length = data[0]

length = int(length)

arr = data[1]

arr = arr.split(" ")

arr = [int(item) for item in arr]


#====================================================================================



def mergeSort(arr, l, limit):

	if l < limit:

		m = (l+(limit-1))//2

		mergeSort(arr, l, m)

		mergeSort(arr, m+1, limit)

		merge(arr, l, m, limit)




#=======================================================================================


def merge(arr, l, m, limit):

	n1 = (m - l) + 1

	n2 = limit - m

	L = [0] * n1

	R = [0] * n2

	for i in range(n1):

		L[i] = arr[l + i]

	for j in range(n2):

		R[j] = arr[m + 1 + j]

	count_1 = 0	

	count_2 = 0	 

	count_3 = l	 

	while (count_1 < n1) and (count_2 < n2):

		if L[count_1] <= R[count_2]:

			arr[count_3] = L[count_1]

			count_1 += 1
			
		else:
		    
			arr[count_3] = R[count_2]
			
			count_2 += 1
			
		count_3 += 1

	while (count_1 < n1):

		arr[count_3] = L[count_1]

		count_1 += 1

		count_3 += 1

	while (count_2 < n2):

		arr[count_3] = R[count_2]

		count_2 += 1

		count_3 += 1
        
#====================================================================================        
        
limit = length - 1        

mergeSort(arr, 0, limit)

index = 0

arr = [str(item) for item in arr]

#====================================================================================

for i in range(length):

    file.write(arr[index] + " ")
    
    index+=1
