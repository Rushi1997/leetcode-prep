# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        stack=[]
        temp=root
        stack.append(temp)
        while stack:
            if temp==None:
                temp=stack.pop()
            else:
                if temp.left!=None and temp.right!=None:
                    stack.append(temp.left)
                    stack.append(temp.right)
                    l=temp.left
                    r=temp.right
                    temp.left=r
                    temp.right=l
                elif temp.left!=None and temp.right==None:
                    stack.append(temp.left)
                    l=temp.left
                    r=None
                    temp.left=r
                    temp.right=l
                elif temp.right!=None and temp.left==None:
                    stack.append(temp.right)
                    l=None
                    r=temp.right
                    temp.left=r
                    temp.right=l
                temp=stack.pop()
        return root
