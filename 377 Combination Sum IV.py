### 377. Combination Sum IV

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # idea, use dp. set dp[i] is the # of unique combinations s.t. sum is i. transition, dp[i] += dp[i-nums[j]], 
        # initial dp[0]=1 and return dp[target]. Time O(n*target), Space O(target)
        dp = [0] * (target + 1)
        dp[0] = 1 # None
        for i in range(1, target+1):
            for j in range(len(nums)):
                if nums[j] <= i:
                    dp[i] += dp[i-nums[j]] # dp[i] = sum_j(dp[i-nums[j]])
        return dp[target]
