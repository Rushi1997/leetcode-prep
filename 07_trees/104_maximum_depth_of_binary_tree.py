# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root==None:
            return 0
        m=0
        stack = []
        stack.append([root,1])
        d=0
        while stack:
            [temp,d]=stack.pop()
            if temp.left!=None and temp.right!=None:
                d+=1
                stack.append([temp.left,d])
                stack.append([temp.right,d])
            elif temp.left==None and temp.right!=None:
                d+=1
                stack.append([temp.right,d])
            elif temp.left!=None and temp.right==None:
                d+=1
                stack.append([temp.left,d])
            m=max(m,d)
        return m
