class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        ans = 0
        n = len(grid[0])
        for i in range(len(grid)):
            for j in range(n):
                
                if grid[i][j] < 0:
                    ans += (n - j) 
                    break
        return ans 