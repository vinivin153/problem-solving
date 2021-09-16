# 938. Range Sum of BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        if root == None:
            return 0
        if low <= root.val <= high:
            sum += root.val
        return (
            self.rangeSumBST(root.right, low, high)
            + self.rangeSumBST(root.left, low, high)
            + sum
        )
