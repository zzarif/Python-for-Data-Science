from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = float("-inf")

        def DFS(root):

            nonlocal diameter
            
            if not root:
                return 0
            
            left_radius = DFS(root.left)
            right_radius = DFS(root.right)

            diameter = max(diameter, left_radius + right_radius)

            return 1 + max(left_radius, right_radius)

        DFS(root)

        return diameter