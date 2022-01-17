"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    
    
    def transform(self,array,schedule):
        res=[]
        #print("res",array)
        for i in array:
            obj=Interval(i[0],i[1])
            res.append(obj)
        return res
    
    def findcommonfree(self,free_prev,free_curr):
        ptr1,ptr2=0,0
        res=[]
        while ptr1<len(free_prev) and ptr2<len(free_curr):
            low=max(free_prev[ptr1][0],free_curr[ptr2][0])
            high=min(free_prev[ptr1][1],free_curr[ptr2][1])
            if low<high:
                res.append([low,high])
            res=res[:]
            
            if free_prev[ptr1][1]==free_curr[ptr2][1]:
                if free_prev[ptr1][1]==100000000:
                    res.append([max(free_prev[ptr1][0],free_curr[ptr2][0]),1000000000])
                ptr1+=1
                ptr2+=1
            elif free_prev[ptr1][1]>free_curr[ptr2][1]:
                ptr2+=1            
            else:
                ptr1+=1
        return res
            
            
            
    
    def freetime(self,array):
        higher_prev=array[0].end
        
        free=[]
        free.append([1,array[0].start])
        for i in range(len(array)):
            if higher_prev==array[i].start:
                continue
            else:
                free.append([higher_prev,array[i].start])
                higher_prev=array[i].end
        
        free.append([array[-1].end,1000000000])
        return free
                
            
    
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        free_prev=self.freetime(schedule[0])
        mn_start=schedule[0][0].start
        print(free_prev)
        for i in range(1,len(schedule)):
            
            free_curr = self.freetime(schedule[i])
            mn_start=min(schedule[i][0].start,mn_start)
            free_prev = self.findcommonfree(free_prev,free_curr)
            print(free_prev)
            if free_prev==[]:
                break
            else:
                continue
        
        if mn_start>=free_prev[0][0]:
            free_prev=free_prev[1:]
        res=self.transform(free_prev[:-1],schedule[0][0])
        return res

##[[[45,56],[89,96]],[[5,21],[57,74]]]
##[[[39,50],[74,88]],[[6,32],[33,34]]]

    