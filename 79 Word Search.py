"""
79. Word Search

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j, 0, m, n, visited):
                    return True
        return False
    def dfs(self, board, word, i, j, pos, m, n, visited):
        # stop criteria, reaches end
        if pos == len(word):
            return True
        if i < 0 or i > m-1 or j < 0 or j > n-1 or visited[i][j] or board[i][j] != word[pos]:
            return False
        visited[i][j] = True
        result = False
        for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            result = result or self.dfs(board, word, i + dx, j + dy, pos + 1, m, n, visited)
        # reset visited[i][j] for next round search
        visited[i][j] = False
        return result

# board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
# word = "ABCCED"
#
# print(Solution().exist(board, word))