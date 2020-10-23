input= [1,1,0,1,1,1]
large=0;
count=0;
for x in input:
    if x==1:
        count=count+1
    else :
        if count>large:
            large=count
        count=0
print( max(large,count))



