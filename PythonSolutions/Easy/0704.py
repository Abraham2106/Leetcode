class Solution(object):
    def search(self, nums, target):
        floor = 0
        value = len(nums)-1
        middle = 0
        while(value >= floor):
            middle = (floor + value) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                floor = middle+1
            if nums[middle] > target:
                value = middle-1
        return -1
            

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        