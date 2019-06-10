"""
212. Word Search II

Input:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Output: ["eat","oath"]

"""
# define Trie class
class Trie:
    def __init__(self):
        self.children = {}
        self.indicator = False

# define TrieNode, insert word into Trie
class TrieNode:
    def __init__(self):
        self.node = Trie()
    def _insert(self, word):
        curr = self.node
        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.indicator = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Naive idea, for each word, use dfs to check whether it's in board or not with word search 79, then
        # append to res. Better idea, use trie to store letter in word, then for each board letter, with dfs to search
        # whether it's in trie or not.
        if not board:
            return []
        m, n = len(board), len(board[0])
        trie = TrieNode()
        for word in words:
            trie._insert(word)
        root = trie.node # pass root into dfs
        res = set() # first set to avoid dumplicate, then convert to list
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                curr_word = []
                self.dfs(board, root, i, j, m, n, visited, curr_word, res)
        return list(res)
    def dfs(self, board, root, i, j, m, n, visited, curr_word, res):
        # out of boundary, not in trie
        if i < 0 or i > m-1 or j < 0 or j > n-1 or visited[i][j] or board[i][j] not in root.children:
            return
        curr_word.append(board[i][j]) # ['o', 'a']
        next_letter = root.children[board[i][j]]
        # append to res when it's complete
        if next_letter.indicator:
            res.add(''.join(curr_word))
        visited[i][j] = True
        self.dfs(board, next_letter, i + 1, j, m, n, visited, curr_word, res)
        self.dfs(board, next_letter, i, j + 1, m, n, visited, curr_word, res)
        self.dfs(board, next_letter, i - 1, j, m, n, visited, curr_word, res)
        self.dfs(board, next_letter, i, j - 1, m, n, visited, curr_word, res)
        visited[i][j] = False
        # key, backtracking for curr_word
        curr_word.pop()

# words = ["oath","pea","eat","rain"]
# board =[['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
#
# print(Solution().findWords(board, words))

