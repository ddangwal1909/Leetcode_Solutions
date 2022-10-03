class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heaped_res = heapq.nlargest(k,nums)[-1]
        return heaped_res