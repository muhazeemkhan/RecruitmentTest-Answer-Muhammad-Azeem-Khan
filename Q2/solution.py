# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Here we are going to implement two pointers, one slow pointer and the other fast pointer.
        # Slow pointer will start at the head of the list where as fast pointer will point to slow + 2 poisition on the list
        # The logic is that we will stop iterating when the slow pointer is one element before the element that we have to delete
        # Intially first Fast and Slow pointers will point to the dummy nodes to tackle egdge cases

        dummy = fast = slow = ListNode(0, next=head)

        # we first move our fast pointer to nth node
        for _ in range(n):
            fast = fast.next;

        while fast.next:
            fast = fast.next;
            slow = slow.next;

        slow.next = slow.next.next;

        return dummy.next;

