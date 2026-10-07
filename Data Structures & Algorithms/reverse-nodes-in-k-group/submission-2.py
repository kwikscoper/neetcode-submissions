# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #constraint: atleast one node is in the linked list
        currHead = nextHead = head
        while True:
            currHead = nextHead
            curr = currHead
            i = 0
            vals = [None] * k
            while curr and i < k:
                vals[i] = curr.val
                curr = curr.next
                i += 1

            nextHead = curr

            if i < k:
                break

            curr = currHead
            for i in range(1, k + 1):
                curr.val = vals[-i]
                curr = curr.next

        return head