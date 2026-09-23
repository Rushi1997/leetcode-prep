# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr=head
        left=None
        while curr!= None:
            temp=curr.next
            curr.next=left
            left=curr
            curr=temp
        return left
