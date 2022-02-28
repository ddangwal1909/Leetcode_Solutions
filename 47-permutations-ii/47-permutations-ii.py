class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        
        res=[]
        def dfs(visited,curr):
            
            if visited[:]==[True]*len(nums) and curr[:] not in res:
                res.append(curr[:])
                return
            else:
                for i in range(len(visited[:])):
                    if visited[i]==False:
                        curr.append(nums[i])
                        visited[i]=True
                        dfs(visited[:],curr[:])
                        curr.pop(len(curr)-1)
                        visited[i]=False
        
        
        visited_global = [False]*len(nums)
        dfs(visited_global[:],[])
        
        return res
            
            
            
                
            