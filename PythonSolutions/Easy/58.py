class Solution(object):
    def lengthOfLastWord(self, s):
        s = s[::-1]
        length = 0

        for i in range(len(s)):
            if s[i] == ' ':
                if length > 0: #Ignores leading whitespaces
                    break
            else:
                length += 1
                
        return length