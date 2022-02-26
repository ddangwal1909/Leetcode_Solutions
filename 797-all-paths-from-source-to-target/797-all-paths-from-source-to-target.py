class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        #print(graph)
        
        res=[]
        
        start = 0
        end = len(graph)-1
        
        def dfs(i,curr_path):
            nonlocal res
            nonlocal end
            
            curr_path.append(i)
            for j in graph[i]:
                #print(curr_path,j)
                if j==end:
                    #print("Here!")
                    curr_path.append(end)
                    res.append(curr_path[:])
                    curr_path.pop(len(curr_path)-1)
                else:
                    dfs(j,curr_path[:])
            curr_path.pop(len(curr_path)-1)
            return
        
        dfs(start,[])
        
        return res
            
            
        
        
        
        
        return []