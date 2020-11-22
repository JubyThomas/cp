nums=[1,1,2]

i=0
while(nums[-1]):
    if(nums[i]==nums[i+1]):
        del nums[i]
        i=i+1   
print(nums)        