# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #reverse second half of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        currNode = slow.next
        slow.next = None
        prevNode = None
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

        curr1 = head
        curr2 = prevNode
        while curr2:
            #store next nodes for each curr node
            next1 = curr1.next
            next2 = curr2.next

            #first half list connects to the second half list curr
            curr1.next = curr2
            #second half list next connects back to first half list next
            curr2.next = next1

            #set curr nodes to the next nodes
            curr1 = next1
            curr2 = next2





