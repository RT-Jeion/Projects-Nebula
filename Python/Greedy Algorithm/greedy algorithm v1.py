x = int(input("Enter The Number:"))
#take a integer number in X

val1, val2, val3 ,val4 = 25, 10, 5, 1
# assign the Value in descending order

val_list= [val1, val2, val3, val4]
# assign values in a list 

Total_val_count = 0

for value in val_list:
    
    val_count = x // value
    x = x % value
    
    Total_val_count += val_count
    

print(f"Total value needed {Total_val_count} times.")