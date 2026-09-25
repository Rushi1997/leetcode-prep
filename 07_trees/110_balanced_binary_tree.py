# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    d=0
    def isBalanced(self, root: TreeNode | None) -> bool:
        self.b=True
        if root==None:
            return True
        def height(root: TreeNode)-> int:
            if root == None:
                return 0
            l=height(root.left)
            r=height(root.right)
            if abs(l-r)>1:
                self.b=False
            return 1 + max(l,r)
        t=height(root)
        return self.b
