self= [1,0,1]
current_node = self.head
        
        # define position
        node_id = 1
        
        # define list of results
        results = []
        
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
                
            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1

reversedName = head[::-1]
number=0
for x in reversedName:
   number=2**x+number
            
print(number)
#large=0;
#count=0;
#for x in input:
#    if x==1:
#        count=count+1
#    else :
#        if count>large:
#            large=count
#        count=0
#print( max(large,count))



