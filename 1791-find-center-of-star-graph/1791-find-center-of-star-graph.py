class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        graph={}
        
        for i in edges:
            if i[0] not in graph.keys():
                graph[i[0]]=[]
                
            if i[1] not in graph.keys():
                graph[i[1]]=[]
                
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        n=len(graph.keys())
        
        for i in graph.keys():
            if len(graph[i])==n-1:
                return i
        
        return 
            
            