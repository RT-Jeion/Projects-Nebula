nums = [4, 9, 3, 7]
target = 10 

d = {}
solution =[]

for i in range(len(nums)):
    x = target - nums[i]
    if x in d:
        
        solution.append(d[x])
        solution.append(i)
        
        #return d[x], i

    d[nums[i]] = i

print(solution)