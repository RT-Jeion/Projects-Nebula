x = int(input("Enter The Number:"))
#take a integer number in X

val_list = [1,]
for i in range(3):
    i += 1
    val_list.append(int(input(f"Enter the value no.{i}: ")))
 
       
print("\n4th value is 1")   
val_list.sort(reverse=True)
print(f"The list of Values is {val_list}\n")

Total_val_count = 0

for value in val_list:
    
    val_count = x // value
    x = x % value
    
    Total_val_count += val_count
    

print(f"Total value needed {Total_val_count} times.")