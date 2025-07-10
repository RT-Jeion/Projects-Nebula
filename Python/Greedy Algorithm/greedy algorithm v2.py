x = int(input("Enter The Number:"))
#take a integer number in X

val1, val2, val3 ,val4 = 25, 10, 5, 1
# assign the Value in descending order

val_list= [val1, val2, val3, val4]
# assign values in a list 


# run loop for the list
for value in val_list:
    
    val_count = x // value
    x = x % value
    
    # take floor value as number count
    
    if value == val1:
        val1_count = val_count
        
    elif value == val2:
        val2_count = val_count
    
    elif value == val3:
        val3_count = val_count
        
    elif value == val4:
        val4_count = val_count 
        
        
              
# Sum all the value counts          
Total_val_count = val1_count + val2_count + val3_count + val4_count

print(f"Total value needed {Total_val_count} times.\n{val1} needed {val1_count} times.\n{val2} needed {val2_count} times.\n {val3} needed {val3_count} times.\n {val4} needed {val4_count} times.")