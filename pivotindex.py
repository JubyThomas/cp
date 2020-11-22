nums=[1,7,3,6,5,6]
pivot=None
leftsum=0


for x in range(0,len(nums)-1):
    rightsum=0
    if(x!=0):
       leftsum=nums[x-1]+leftsum
    for y in range(x+1,len(nums)):
        rightsum=nums[y]+rightsum
    if(leftsum==rightsum):
        pivot=x
        break

if(pivot is None):
    pivot=-1

print(pivot)