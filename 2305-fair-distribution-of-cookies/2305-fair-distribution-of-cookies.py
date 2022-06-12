class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        optim_unfair=math.inf
        
        dist=[0]*k
        
        if len(cookies)==k:
            return max(cookies)
        
        def bt(idx):
            nonlocal optim_unfair
            if idx>=len(cookies):
                optim_unfair=min(optim_unfair,max(dist))
                return
            else:
                for j in range(k):
                    dist[j]+=cookies[idx]
                    bt(idx+1)
                    dist[j]-=cookies[idx]
            return
        
        bt(0)
        
        return optim_unfair
            
        