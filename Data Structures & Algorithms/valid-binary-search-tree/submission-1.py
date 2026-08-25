# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(leftbound, node, rightbound):
            if not node:
                return True
            if not (leftbound < node.val < rightbound):
                return False
            
            return isValid(leftbound, node.left, node.val) and isValid(node.val, node.right, rightbound)

        return isValid(float('-inf'), root, float('inf'))