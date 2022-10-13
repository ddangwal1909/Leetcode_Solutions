import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap=[]
        
        heappush(heap,(nums1[0]+nums2[0],0,0))
        res=[]
        visited=set((0,0))
        i=0
        j=0
        while heap:
            if k==0:
                return res
            else:
                val=heappop(heap)
                res.append((nums1[val[1]],nums2[val[2]]))
                k-=1
                if val[1]+1<len(nums1) and (val[1]+1,val[2]) not in visited:
                    heappush(heap,(nums1[val[1]+1]+nums2[val[2]],val[1]+1,val[2]))
                    visited.add((val[1]+1,val[2]))
                if val[2]+1<len(nums2) and (val[1],val[2]+1) not in visited:
                    heappush(heap,(nums1[val[1]]+nums2[val[2]+1],val[1],val[2]+1))
                    visited.add((val[1],val[2]+1))
        
        return res
                
                
                
            