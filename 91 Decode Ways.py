'''
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''

class Solution:
    def numDecodings(self, s):
        # idea, use dp. set dp[i] is the total # of ways to decode it. dp[i] = dp[i-1] (if s[i-1] != '0') + dp[i-2]
        # (if 10 <= s[i-2:i] <= 26). initiate, dp[0] = 0, dp[1] = 1 if s[0] != '0'. Time and Space O(n), sliding window
        # reduce space to O(1).
        if not s:
            return 0
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, n+1):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[n]

    def Decodings(self, s):
        # use dfs to output all possible decodings. stop criteria, when pos reaches end.
        pos = 0
        res = []
        tmplist = []
        self.dfs(pos, s, tmplist, res)
        return res

    def dfs(self, pos, s, tmplist, res):
        if pos == len(s):
            res.append(''.join(tmplist))
            return
        if s[pos] != '0':
            ones = chr(int(s[pos]) - int('1') + ord('A'))
            self.dfs(pos+1, s, tmplist + [ones], res)
        if pos < len(s) - 1 and (s[pos] == '1' or (s[pos] == '2' and s[pos + 1] <= '6')):
            twos = chr(int(s[pos: pos + 2]) - int('1') + ord('A'))
            self.dfs(pos + 2, s, tmplist + [twos], res)

if __name__ == '__main__':
    test = Solution()
    print(test.numDecodings('226'))
    print(test.numDecodings('12'))
    print(test.numDecodings('100'))
    print(test.Decodings('100'))
    print(test.Decodings('226'))


