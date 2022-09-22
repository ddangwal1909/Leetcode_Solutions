class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = {}
        
        for i in edges:
            if i[0] not in graph.keys():
                graph[i[0]]=[]
            if i[1] not in graph.keys():
                graph[i[1]]=[]
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        if len(edges)==0:
            if source==destination:
                return True
            else:
                return False
        
        visited=[0 for i in range(max(graph.keys())+1)]
        
        for i in range(len(visited)):
            if i not in graph.keys():
                visited[i]=1
            
        print(visited)
        print(graph)
        result=False
        @lru_cache(maxsize=1000)
        def helper(curr_node):
            nonlocal result
            nonlocal destination
            nonlocal visited
            nonlocal graph
            print(curr_node)
            visited[curr_node]=1
            
            if result==True:
                return
            elif curr_node==destination:
                result = True
                return
            else:
                for i in graph[curr_node]:
                    if visited[i]==0:
                        helper(i)
            return
        
        helper(source)
        
        return result