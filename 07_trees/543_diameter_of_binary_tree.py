# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    d=0
    def height(self, root: Optional[TreeNode]) ->int:
        if root ==None:
            return 0
        l= self.height(root.left)
        r=self.height(root.right)
        self.d=max(self.d,l+r)
        return 1+max(l,r)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0

        t=self.height(root)
        return self.d
