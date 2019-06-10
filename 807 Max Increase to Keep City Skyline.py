### 807. Max Increase to Keep City Skyline
#Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
#Output: 35
#Explanation: 
#The grid is:
#[ [3, 0, 8, 4], 
#  [2, 4, 5, 7],
#  [9, 2, 6, 3],
#  [0, 3, 1, 0] ]
#
#The skyline viewed from top or bottom is: [9, 4, 8, 7]
#The skyline viewed from left or right is: [8, 7, 9, 3]
#
#The grid after increasing the height of buildings without affecting skylines is:
#
#gridNew = [ [8, 4, 8, 7],
#            [7, 4, 7, 7],
#            [9, 4, 8, 7],
#            [3, 3, 3, 3] ]

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # idea, first obtain row/col max, then loop row/col to find the gridNew[i][j]=min(row_max[i], col_max[j]), gridNew[i][j]-grid[i][j] is the increasing. Time O(mn), Space O(max(m,n)).
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        row_max = [0 for i in range(m)]
        col_max = [0 for j in range(n)]
        # for row_max
        for i in range(m):
            for j in range(n):
                row_max[i] = max(row_max[i], grid[i][j])
        # for col_max
        for j in range(n):
            for i in range(m):
                col_max[j] = max(col_max[j], grid[i][j])
        # loop row/col to find increasing
        res = 0
        for i in range(m):
            for j in range(n):
                res += min(row_max[i], col_max[j])-grid[i][j]
        return res
        
## follow up, only given 
#row_max = [9, 4, 8, 7]
#col_max = [8, 7, 9, 3]  

## use binary search, sort first, O(nlogm+mlogn); then binary search for each row. Time O(nlogm)          
class Solution(object):
    def maxIncreaseKeepingSkyline(self, row_max, col_max):
        row_max.sort()
        col_max.sort()
        m, n = len(row_max), len(col_max)
        res = 0
        for j in range(n):
            i = self.bs(row_max, col_max[j]) # j is the first val > col_max[j]
            res += sum(row_max[:i]) + col_max[j]*(n-i)
        return res
    
    def bs(self, row_max, col_val):
        m = len(row_max)
        left, right = 0, n-1
        while left < right:
            mid = left + (right-left)//2
            if row_max[mid] <= col_val:
                left = mid + 1
            else:
                right = mid - 1
        return left

#print(Solution().maxIncreaseKeepingSkyline(row_max, col_max))
        