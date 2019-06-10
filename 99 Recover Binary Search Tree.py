"""
99. Recover Binary Search Tree

Input: [3,1,4,null,null,2]
  3
 / \
1   4
   /
  2
Output: [2,1,4,null,null,3]
  2
 / \
1   4
   /
  3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        # naive idea, use inorder traversal and save to array, sort the array, and compare two nodes that differ. Then inorder
        # traversal again, then if node.val == diff[0], node.val = diff[1], elif node.val == diff[1], node.val == diff[0]
        if not root:
            return None
        array = []
        self.inorder(root, array)
        sort_array = sorted(array)
        diff = []
        for x, y in zip(array, sort_array):
            if x != y:
                diff = [x, y]
        self.dfs(root, diff)

    def inorder(self, root, array):
        if not root:
            return
        self.inorder(root.left, array)
        array.append(root.val)
        self.inorder(root.right, array)

    def dfs(self, root, diff):
        if not root:
            return
        self.dfs(root.left, diff)
        if root.val == diff[0]:
            root.val = diff[1]
        elif root.val == diff[1]:
            root.val = diff[0]
        self.dfs(root.right, diff)

    def recoverTree2(self, root):
        # use global prev node, inorder traversal, if prev.val >= root.val, then first = prev; second = root; move
        # forward prev.
        if not root:
            return
        self.prev = TreeNode(-sys.maxsize)
        self.first, self.second = None, None
        self.inorder2(root)
        # swap val
        self.first.val, self.second.val = self.second.val, self.first.val
    def inorder2(self, root):
        if not root:
            return
        self.inorder2(root.left)
        if self.prev.val >= root.val:
            if not self.first:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.inorder2(root.right)

root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.right.left = TreeNode(2)
# #
# Solution().recoverTree(root)
# print(root.val, root.left.val, root.right.val, root.right.left.val)

# Solution().recoverTree2(root)
# print(root.val, root.left.val, root.right.val, root.right.left.val)

