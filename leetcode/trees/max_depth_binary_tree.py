from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        max_depth = float("-inf")

        def DFS(root, depth):

            if not root:
                return max(max_depth, depth)
            
            return max(DFS(root.left, depth+1), DFS(root.right, depth+1))

        return DFS(root, 0)