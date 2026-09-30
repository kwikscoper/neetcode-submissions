# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        nodes = 0
        curr = head
        while curr:
            nodes += 1
            curr = curr.next

        nodeBeforeDel = nodes - n
        curr = dummy
        for i in range(nodeBeforeDel):
            curr = curr.next

        curr.next = curr.next.next

        return dummy.next