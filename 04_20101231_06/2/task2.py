fdata = open('input.txt')

fdata= fdata.read()

file = open('output.txt', 'w')

data = fdata.split('\n')

sequence = data[0]

prediction = data[1]

prediction_2 = data[2]

number_of_zones = len(sequence)

length = len(prediction)


def LCS(sequence, prediction, number_of_zones, length, prediction_2):
    
    L = []
    
    count_3 = 0
    
    for x in range(2):
    
        for i in range(number_of_zones + 1):
            
            L.append([0]*(length + 1))
    
        for i in range(number_of_zones + 1):
        
            for j in range(length + 1):
        
                if i == 0 or j == 0:
        
                    L[i][j] = 0
        
                elif sequence[i-1] == prediction[j-1]:
        
                    L[i][j] = L[i-1][j-1] + 1
        
                else:
        
                    L[i][j] = max(L[i-1][j], L[i][j-1])
    
        index = L[number_of_zones][length]
    
        result = [""] * index
    
        count_1 = number_of_zones
        
        count_2 = length
            
        while True:
            
            if (count_1 > 0) and (count_2 > 0):
    
                if sequence[count_1-1] == prediction[count_2-1]:
            
                    result[index-1] = sequence[count_1-1]
            
                    count_1 -= 1
            
                    count_2 -= 1
            
                    index -= 1
        
                elif L[count_1-1][count_2] > L[count_1][count_2-1]:
                
                    count_1 -= 1
                
                else:
                
                    count_2 -= 1
                    
            else:
        
                if "" in result:
                    
                    result.remove("")
                    
                break   
        
        if count_3 < 1:
            
            loop = len(result)
            
            value = ""
            
            for i in range(loop):
                
                value = value + result[i]
                
            sequence = value
            
            number_of_zones = len(sequence)
            
            prediction = prediction_2
            
            count_3+=1
    
    print(len(result))
    
    file.write(str(len(result)))

LCS(sequence, prediction, number_of_zones, length, prediction_2)