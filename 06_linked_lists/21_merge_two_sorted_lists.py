# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        temp = ListNode(0)
        start =temp
        while list1!=None or list2!=None:
            if list1!=None and list2!=None:
                if list1.val <=list2.val:
                    t=ListNode(list1.val)
                    temp.next=t
                    list1=list1.next
                else:
                    t=ListNode(list2.val)
                    temp.next=t
                    list2=list2.next
            elif list1==None and list2!=None:
                temp.next=list2
                return start.next
            elif list2==None and list1!=None:
                temp.next=list1
                return start.next
            temp=temp.next
        return start.next
