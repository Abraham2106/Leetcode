class Solution(object):
    def minimumOperations(self, nums):
        # One liner using return len(set(nums)-{0})
        # the array without dupli~kates [Titlecard] 
        # The array without duplicates and without 0 is the minimum number needed 
        count = 0 

        while sum(nums) != 0:

            smol = float("inf")

            for i in range(len(nums)):

                if nums[i] < smol and nums[i] != 0:
                    smol = nums[i]

            count += 1

            for i in range(len(nums)):
                if nums[i] == 0:
                    continue

                else:
                    nums[i] = nums[i]-smol
                    
        return count
        """
        :type nums: List[int]
        :rtype: int
        """
        