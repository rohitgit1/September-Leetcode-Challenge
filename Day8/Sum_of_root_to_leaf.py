# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode, sum_=0) -> int:
        if not root:
            return 0
        
        sum_ = sum_*2 + root.val
        
        if root.left or root.right:
            return self.sumRootToLeaf(root.left,sum_) + self.sumRootToLeaf(root.right,sum_)
        else:
            return sum_
