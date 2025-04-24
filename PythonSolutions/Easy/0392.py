class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True

        for i in range(len(t)):

            if s[0] == t[i]:
                s = s[1:]

            if not s:
                return True
                
        return False