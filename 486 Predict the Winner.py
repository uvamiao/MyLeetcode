### Mock interview
### 486. Predict the Winner

#Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of
#the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number
#will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.
#Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.
#
#Example 1:
#Input: [1, 5, 2]
#Output: False

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # idea, use two dimension dp. set dp[i][j] is the max more scores Play 1 can get from i to j than Play 2.
        # transition function, dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1]), i<j, i backward, j forward.
        # play 1 picks nums[i], then play 2 can earn dp[i+1][j] more scores, so nums[i]-dp[i+1][j]. 
        # initialize dp[i][i]=nums[i], return dp[0][len-1]>=0, O(n^2) time, O(n^2) space.
        n = len(nums)
        if not nums:
            return False
        dp = [[0 for i in range(n)] for j in range(n)]
        # loop i and j
        for i in range(n-1,-1,-1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        return dp[0][n-1]>=0

#print(Solution().PredictTheWinner([1,5,2]))

class Solution2(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # idea, use two dimension dp. set dp[i][j] is the max more scores Play 1 can get from i to j than Play 2.
        # transition function, dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1]), i<j, i backward, j forward.
        # play 1 picks nums[i], then play 2 can earn dp[i+1][j] more scores, so nums[i]-dp[i+1][j]. 
        # initialize dp[i][i]=nums[i], return dp[0][len-1]>=0. O(n^2) time, O(n) space, rolling array. 
        n = len(nums)
        if not nums:
            return False
        dp = [[0 for j in range(n)] for i in range(2)]
        # loop i and j
        for i in range(n-1,-1,-1):
            for j in range(i, n):
                if i == j:
                    dp[i%2][j] = nums[i]
                else:
                    dp[i%2][j] = max(nums[i]-dp[(i+1)%2][j], nums[j]-dp[i%2][j-1])
        return dp[0][n-1]>=0
