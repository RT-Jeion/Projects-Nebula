nums = [4, 5, 9, 5]
target = 10 

d = {}
solution =[]

for i in range(len(nums)):
    d[nums[i]] = i

for i in range(len(nums)):
    
    x = target - nums[i]
    
    if x in nums and d[x] != nums[i] :
        solution.append(i)
        solution.append(d[x])
        
        break 
        #return d[x], i
        

print(solution)