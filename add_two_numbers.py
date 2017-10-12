# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l3 = ListNode(0)
        l4 = l3
        carry = 0
        while l1 != None and l2 != None:
            l3.val = l1.val + l2.val + carry
            carry = 0
            if l3.val > 9:
                carry = l3.val / 10
                l3.val = l3.val % 10
            l1 = l1.next 
            l2 = l2.next
            if l1 != None and l2 != None:
                l3.next = ListNode(0)
                l3 = l3.next
            
        while l1 != None:
            l3.next = ListNode(0)
            l3 = l3.next
            l3.val = l1.val + carry
            carry = 0
            if l3.val > 9:
                carry = l3.val / 10
                l3.val = l3.val % 10
            l1 = l1.next        
        
        while l2 != None:
            l3.next = ListNode(0)
            l3 = l3.next
            l3.val = l2.val + carry
            carry = 0
            if l3.val > 9:
                carry = l3.val / 10
                l3.val = l3.val % 10
            l2 = l2.next 
                
        while carry != 0:
            l3.next = ListNode(0)
            l3 = l3.next
            l3.val = carry
            carry = 0
            if l3.val > 9:
                carry = l3.val / 10
                l3.val = l3.val % 10 
                
        l3.next = None
            
        return l4