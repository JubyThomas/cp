
arr=[1,0,2,3,0,4,5,0]
i =0
x=len(arr)-1
print ("orihinial array")
print(arr)
while i<=x:
    if(arr[i] == 0):
        arr.insert(i+1, 0)
        print (arr)
        print (i)
        
        i+= 2
    else:
        i+=1
print(arr)
