class Solution(object):
    def convertTime(self, current, correct):

        total_current = int(current[:2]) * 60 + int(current[3:])
        total_correct = int(correct[:2]) * 60 + int(correct[3:])

        total_ans = total_correct - total_current

        ans = 0

        for value in [60, 15, 5, 1]:

            ans += total_ans // value
            total_ans %= value

        return ans
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        