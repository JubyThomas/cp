l=[]
nums=[3,3]
target=6       
for x,val in enumerate(nums):
            z=target-val
            if z in nums and nums.index(z)!=x:
                l.append(x)
                l.append(nums.index(z))  
                break
print(l)    
        