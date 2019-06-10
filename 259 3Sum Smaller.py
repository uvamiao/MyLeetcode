"""
Input: nums = [-2,0,1,3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that
satisfy the condition nums[i] + nums[j] + nums[k] < target.
"""

class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        n = len(nums)
        cnt = 0
        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                sm = nums[i] + nums[left] + nums[right]
                if sm >= target:
                    right -= 1
                else:
                    cnt += right - left
                    left += 1
        return cnt

if __name__ == '__main__':
    nums = [-2, 0, 1, 3]
    target = 2
    print(Solution().threeSumSmaller(nums, target))
