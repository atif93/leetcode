# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 != None:
            if l2 != None:
                if l1.val <= l2.val:
                    l3 = ListNode(l1.val)
                    l1 = l1.next
                else:
                    l3 = ListNode(l2.val)
                    l2 = l2.next
            else:
                return l1
        else:
            if l2 != None:
                return l2
            else:
                return None
            
        temp = l3
        while l1 != None or l2 != None:
            if l1 != None and (l2 == None or l1.val <= l2.val):
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                temp = temp.next
                l2 = l2.next
        return l3