"""
261. Graph Valid Tree

Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
Example 1:
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0]and thus will not appear together in edges.

"""

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # build graph, use bfs + visited to check whether there is cycle or not; finally, check whether the # of visited is n.
        if n <= 0:
            return False
        graph = collections.defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        visited = set()
        queue = collections.deque()
        queue.append(0)
        while queue:
            node = queue.popleft()
            if node in visited:
                return False
            visited.add(node)
            for neigh in graph[node]:
                queue.append(neigh)
                graph[neigh].discard(node)
        return len(visited) == n

# import collections
#
# n = 5
# edges = [[0,1], [0,2], [0,3], [1,4]]
#
#
# print(Solution().validTree(n, edges))
#
# print(Solution().validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))
