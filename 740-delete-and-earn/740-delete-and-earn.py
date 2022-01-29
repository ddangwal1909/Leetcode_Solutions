class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        sm=sum(nums)
        lst=list(set(nums))
        mx_num=max(lst)
        map_values={key:key*nums.count(key) for key in range(mx_num+1)}
                   
        print(map_values)
        
        if len(lst)==1:
            return map_values[lst[0]]
        else:
            dp=[0]*(mx_num+1)
            dp[0]=0
            dp[1]=map_values[1]
            for i in range(2,mx_num+1):
                dp[i]=max(dp[i-2]+map_values[i],dp[i-1])
            
            
            return dp[mx_num]