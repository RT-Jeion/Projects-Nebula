#Take the maximum value 
x = input("Enter the max number You want to print : ")
name = input("Enter The Name: ")

# Measure the max value's length 
len_x = len(x)

# 
for i in range (0,int(x)):
    prefix = ""
    i += 1
    i = str(i)
    len_i = len(i)
    len_gap = len_x - len_i
    
    for _ in range(len_gap):
       prefix += "0"

    print (f"{prefix}{i}.{name}")
