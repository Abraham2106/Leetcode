class Solution:

    def findTheDifference(self, s: str, t: str) -> str:
        s_ASCII = sum(ord(i) for i in s)
        t_ASCII = sum(ord(j) for j in t)
        return chr(t_ASCII - s_ASCII)
        
        
        