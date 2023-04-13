nums = [1,2,3,4,5,6,7,8,9]
nums.append(10) #adds to the end of list.
nums.insert(0,"A")#inserts value where you want.
nums.extend(["A","B","C"])#can connect two lists.
nums.remove(5)#to remove from list by searching.
del nums[5]#to remove by indexing.

#nested list.
nums = [1,2,3,[3.1,3.2,3.3],4,5]
print (nums[3][-1])

print(nums)