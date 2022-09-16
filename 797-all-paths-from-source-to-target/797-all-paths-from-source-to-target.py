class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        start=0
        end=len(graph)-1
        res=[]
        
        def helper(i,curr):
            nonlocal res
            nonlocal graph
            nonlocal end 
            print(curr)
            if i==end:
                curr.append(i)
                res.append(curr[:])
                curr=curr[:-1]
            
            else:
                curr.append(i)
                for j in graph[i]:
                    helper(j,curr[:])
                curr=curr[:-1]
            return
        
        helper(start,[])
        
        return res
        
        