### Find the lowest number/value in an array

my_array = [7, 12, 9, 4, 11]
minVal = my_array[0]    # Step 1

for i in my_array:      # Step 2
    if i < minVal:      # Step 3
        minVal = i
        
print('Lowest value: ',minVal) # Step 4


### Find the highest number/value in an array

my_array = [7, 12, 9, 4, 11]
maxVal = my_array[0]    # Step 1

for i in my_array:      # Step 2
    if i > maxVal:      # Step 3
        maxVal = i
        
print('Lowest value: ',maxVal) # Step 4
