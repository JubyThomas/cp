 s = "hooraaaaaaaaaaay"
 x,count,y=0,0,1
 maxC=0
     while x<len(s)-1:
                    
        while y <len(s)-1:
           if(s[x]==s[y+1]):
                        count+=1
                    else :
                        x=x+1 
                        break
                    y+=1
                maxC=max(count,maxC)    
                x+=count 