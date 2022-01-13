class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        
        curr_cap=capacity
        i=0
        steps=0
        while(i<len(plants)):
            if i==0 :
                if curr_cap<plants[i]:
                    steps+=2
                    curr_cap=capacity-plants[i]
                else:
                    curr_cap=curr_cap-plants[i]
                    steps+=1
            
            else:
                if curr_cap<plants[i]:
                    steps+=2*i
                    steps+=1
                    curr_cap=capacity-plants[i]
                else:
                    curr_cap=curr_cap-plants[i]
                    steps+=1
            
            i+=1
        
        ''' 
        while i<len(plants):
            current_left = plants[i]
            if i==0:
                if curr_cap<current_left:
                    current_left=plants[i]-curr_cap
                    steps+=2*(int(current_left/capacity)+1)
                    curr_cap = capacity*(int(current_left/capacity)+1)-current_left
                else:
                    curr_cap = curr_cap-plants[i]
                    steps+=1
            else:
                if curr_cap<current_left:
                    current_left = current_left-curr_cap
                    steps+=1
                    times=int(current_left/capacity)+1
                    if times>1:
                        steps=steps+(i*2)+((i+1)*2)*(times-1)
                    else:
                        steps=steps+(i*2)
                    curr_cap=(capacity*times) - current_left
                else:
                    steps+=1
                    curr_cap=curr_cap-plants[i]
            i+=1
        '''
        return steps
        