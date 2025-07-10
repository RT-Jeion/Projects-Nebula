x = int(input("Enter The Number:"))
val1 = int(input("Enter Value no.1:"))
val2 = int(input("Enter Value no.2:"))
val3 = int(input("Enter Value no.3:"))
# Take a integer and 3 value 
    
    
val4 = 1
print(f'\nValue no.4 is"{val4}"') # 4th value is predifined 1
    
val_list= [val1, val2, val3, val4]
val_list.sort(reverse=True) # assing value in a list and sort in descending order 
print(f"The list of Values is {val_list}\n")
    
    
for value in val_list: # run loop in list
        
    val_count = x // value # take floor value as number count
       
    x = x % value
        
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
    
print(f"Total value needed {Total_val_count} times.\n\n{val1} needed {val1_count} times.\n{val2} needed {val2_count} times.\n{val3} needed {val3_count} times.\n{val4} needed {val4_count} times.")
        