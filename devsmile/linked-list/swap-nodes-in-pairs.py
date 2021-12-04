# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head

            prev.next = tmp

            head = head.next
            prev = prev.next.next

        return root.next


# Recursive Solution
class Solution_Recursive:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            tmp = head
            head = head.next
            tmp.next = self.swapPairs(head.next)
            head.next = tmp
        return head
