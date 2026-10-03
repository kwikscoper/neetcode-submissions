# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for head in lists:
            curr = head
            while curr:
                heapq.heappush(minHeap, curr.val)
                curr = curr.next
        
        dummy = ListNode()
        currNode = dummy
        while minHeap:
            nextNode = ListNode()
            currNode.next = nextNode
            currNode = nextNode
            currNode.val = heapq.heappop(minHeap)

        return dummy.next