nums1=[1,2,3,0,0,0]
nums2=[2,5,6]

index=5
m,n=2,2

print(n)

while(index>0):

   if(nums2[n]>=nums1[m] and n>0):
    nums1[index]=nums2[n]
    m=m-1
    n=n-1
    index=index-1
   else:
    nums1[index]=nums1[m]
    m=m-1
    index=index-1
 
nums1.sort()   

print(nums1)       