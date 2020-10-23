nums1=[1,2,3,0,0,0]
n=3
x=0
y=0
nums2=[2,5,6]
  
if n>0:
    while x>=0 and x<len(nums1)-1 :
        while y>=0 and y<len(nums2)-1:
            if  nums2[x] <=nums1[y]:
                nums1.pop(-1)
                nums1.insert(x,nums2[y=])
                nums2.pop(0)
            
        x=x+1
        y=y+1              
print(nums1)            