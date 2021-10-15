# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = 0
        if root == None:
            return 0

        if root.val > high:
            s = self.rangeSumBST(root.left, low, high)
        elif root.val < low:
            s = self.rangeSumBST(root.right, low, high)
        else:
            s = (
                root.val
                + self.rangeSumBST(root.left, low, high)
                + self.rangeSumBST(root.right, low, high)
            )

        return s
