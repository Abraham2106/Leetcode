"""Doesn't works TLE and not optimal"""
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        
        def searchThru(l, r):
            count = 0
            for i in range(l, r + 1):  
                if nums[i] % modulo == k:
                    count += 1

            return count % modulo == k

        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if searchThru(i, j):
                    ans += 1
                    
        return ans
        

            