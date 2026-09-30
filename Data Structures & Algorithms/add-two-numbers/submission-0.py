# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        
        curr1 = l1
        i = 0
        while curr1:
            num1 += curr1.val * 10**i
            curr1 = curr1.next
            i += 1

        curr2 = l2
        i = 0
        while curr2:
            num2 += curr2.val * 10**i
            curr2 = curr2.next
            i += 1

        total = num1 + num2

        if total == 0:
            return ListNode(0)
            
        dummy = ListNode()
        curr = dummy
        while total > 0:
            curr.next = ListNode(total % 10)
            total //= 10
            curr = curr.next

        return dummy.next