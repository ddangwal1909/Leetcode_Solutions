class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        lst = s.split(' ')
        res=' '.join(lst[:k])
        return res