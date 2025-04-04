# if's avalanche 
class Solution(object):
    def triangleType(self, nums):
        len_nums = len(nums)
        if len_nums != 3:
            return "none"
        val = False
        val2 = True
        for i in range(len_nums):
            if nums[i-3] + nums[i-2] <= nums[i-1]:
                return "none"
            if nums[i-3] == nums[i-2]:
                val = True
            else:
                val2 = False
        if val2:
            return "equilateral"
        if val:
            return "isosceles"
        else:
            return "scalene"

        
        """
        :type nums: List[int]
        :rtype: str
        """
        