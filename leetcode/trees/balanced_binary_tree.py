from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def DFS(root):
    
            if not root:
                return (0, True)
            
            lRadius = DFS(root.left)
            rRadius = DFS(root.right)

            balanced = lRadius[1] and rRadius[1] and abs(lRadius[0] - rRadius[0]) <= 1

            return (1 + max(lRadius[0], rRadius[0]), balanced)
        
        return DFS(root)[1]
