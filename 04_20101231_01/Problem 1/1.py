fdata = open('input.txt')

fdata= fdata.read()

file = open('output.txt', 'w')

data = fdata.split('\n')

rfile = open('record.txt', 'w')

count = 0

odd = 0

even = 0

no = 0


for i in range(len(data)-1):
    
    value = data[count]
    
    number, word = value.split(" ")

    def isPalindrome(word):
        
        if (word == ""):
            
            return "Not palindrome"
        
        else:
            
            N = len(word)
            
            for i in range(N//2):
                
                if word[i] != word[N-1-i]:
                    
                    return "Not palindrome"
                
        return "Palindrome"
        
    #=========================================================================    
        
    def parityChecker(number):
        
        try:
            
            number = int(number)
            
        except:
            
            number = float(number)   
    
            
        if (type(number) == float):
            
            result = "no parity"
            
        elif (number % 2 == 0):
            
            result = "even parity"
            
        else:
            
            result = "odd parity"
            
        return result
    
    
    value_1 = isPalindrome(word)
    
    value_2 = parityChecker(number)
    
    file.write(number + " has " + value_2 + " and " + word + " is an " + value_1 + "\n")
    
    
#==========================================================================    
    
    try:
        
        magnitude = int(number)
        
    except:
        
        magnitude = float(number)   

        
    if (type(magnitude) == float):
        
        no+=1
        
    elif (magnitude % 2 == 0):
        
        even+=1
        
    else:
        
        odd+=1
        
    count+=1    

odd_parity = int(odd * 100 / count)

even_parity = int(even * 100 / count)

palindrome = odd + even

palindrome = int(palindrome * 100 / count)

non_palindrome = int(100 - palindrome)

noParity = int(no * 100 / count)
        
    
rfile.write("Percentage of odd parity: " + str(odd_parity) + "%" + "\n")
    
rfile.write("Percentage of even parity: " + str(even_parity)+ "%" + "\n")

rfile.write("Percentage of no parity: " + str(noParity)+ "%" + "\n")

rfile.write("Percentage of palindrome: " + str(non_palindrome)+ "%" + "\n")

rfile.write("Percentage of non-palindrome: " + str(palindrome)+ "%")

    
#===========================================================================    

    
      
