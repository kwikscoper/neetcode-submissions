# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #find halfway point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half
        currNode = slow.next
        slow.next = None
        prevNode = None
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

        currFront = head
        currBack = prevNode
        while currFront and currBack:
            if currFront.val == currBack.val:
                currFront = currFront.next
                currBack = currBack.next
            else:
                return False

        return True