### 52. N-Queens II

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # idea, similar recursion idea as n-queens, but use count to get the # of distinct solutions. Time O(n!), Space O(n)
        # control variable to check whether it's valid for col, diag and anti_diag
        self.col = [False] * n
        self.diag = [False] * 2 * n
        self.anti_diag = [False] * 2 * n
        self.count = 0 # initiate count 
        self.recursive(0, n) # recursive row, n
        return self.count
    # define recursive function
    def recursive(self, row, n):
        # stop criteria
        if row == n:
            self.count += 1
        else:
            for i in range(n):
                if not self.col[i] and not self.diag[row+i] and not self.anti_diag[n+row-i]:
                    self.col[i] = self.diag[row+i] = self.anti_diag[n+row-i] = True
                    # recursion
                    self.recursive(row+1, n)
                    # release to False again for next Solution
                    self.col[i] = self.diag[row+i] = self.anti_diag[n+row-i] = False
    

