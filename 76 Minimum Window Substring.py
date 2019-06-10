'''
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
'''
import collections

class Solution(object):
    def minWindow(self, s, t):
        # idea, first obtain the frequency of T, use sliding window, i and j, move j until
        # there is no missing letters, while loop to move left to find the true start, until can't cover T;
        # update global [left, right], then move left one step forward, for the next round of iteration on j.
        count = collections.Counter(t)
        lent = len(t)
        left, right = 0, 0 # indicate left, right for result
        i = 0 # [i, j] is the sliding window
        for j, val in enumerate(s):
            if count[val] > 0:
                lent -= 1
            count[val] -= 1
            if lent == 0:
                while i < j and count[s[i]] < 0:
                    count[s[i]] += 1
                    i += 1
                if right == 0 or j + 1 - i < right - left:
                    left, right = i, j + 1 # [i, j+1]
                # move forward i to i + 1
                count[s[i]] += 1
                i += 1
                lent += 1
        return s[left : right]

# print(Solution().minWindow("ADOBECODEBANC", "ABC"))