"""
528. Random Pick with Weight

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.
Note:
1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]

"""

class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        sm = 0
        self.psum = []
        for weight in w:
            sm += weight
            self.psum.append(sm)

    def pickIndex(self):
        """
        :rtype: int
        """
        # use binary search to find the first index such that self.psum[index] >= target
        target = random.randint(1, self.psum[-1])
        left, right = 0, len(self.psum) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.psum[mid] >= target:
                right = mid
            else:
                left = mid
        if self.psum[left] >= target:
            return left
        return right


    def PickKeys(self, Keys):
        # use binary search to find the first index such that self.psum[index] >= target
        val = random.random() # random float num in [0, 1]
        target = self.psum[-1] * val # min + (max - min) * val
        left, right = 0, len(self.psum) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.psum[mid] >= target:
                right = mid
            else:
                left = mid
        if self.psum[left] >= target:
            return Keys[left]
        return Keys[right]

# import random
# import collections
#
# w = [1, 2, 3]
# obj = Solution(w)
#
# tmp = []
# for i in range(1000):
#     tmp.append(obj.pickIndex())
#
# freq = collections.Counter(tmp)
# print(freq)
#
#
# ## follow up, w is float
#
# w2 = [1.5, 3.0, 4.5]
# Keys = ['a', 'b', 'c']
# obj2 = Solution(w2)
#
# tmp2 = []
# for i in range(1000):
#     tmp2.append(obj2.PickKeys(Keys))
#
# freq2 = collections.Counter(tmp2)
#
# print(freq2)






