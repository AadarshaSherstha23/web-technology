nums = [2,4,6]
nums_sqr=[]
for i in nums:
    nums_sqr.append(i**2)    
print(nums_sqr)   

[i**2 for i in nums]


nums= [1,2,3,4,5,6]
even_numbers =[x for x in nums if x % 2==0]
print(even_numbers)

