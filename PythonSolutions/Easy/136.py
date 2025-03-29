class Solution(object):
    def singleNumber(self, nums):
        total_sum = sum(nums)
        set_nums = set(nums)
        total_set = sum(set_nums)*2
        return total_set - total_sum
        """
        :type nums: List[int]
        :rtype: int
        """
        