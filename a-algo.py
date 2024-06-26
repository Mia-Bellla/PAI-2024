# Simple Python program to print the simple triangle pyramid  
n = int(input("Enter the number of rows: "))    
# Here, we are declaring the integer variable to store the input rows  
m = (2 * n) - 2     # Here, the m is used for number of spaces  
# Here, we are declaring an outer loop to handle number of rows  
for i in range(0, n):    
     # Here, we are declaring an for loop to handle number of spaces  
    for j in range(0, m):    
        print(end=" ")    
    m = m - 1      # Here, we are decrementing the m after each loop    
# Here, we are declaring an outer loop to print the pattern      
for j in range(0, i + 1):    
        # Here, we are printing the full Triangle pyramid using stars    
        print("* ", end=' ')    
print(" ") 