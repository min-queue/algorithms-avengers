# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_node = ListNode()
        odd_head = odd_node

        even_node = ListNode()
        even_head = even_node
        cnt = 1
        while head is not None:
            if cnt % 2 == 0:
                even_head.next = ListNode(val=head.val)
                even_head = even_head.next
            else:
                odd_head.next = ListNode(val=head.val)
                odd_head = odd_head.next
            head = head.next
            cnt += 1

        odd_head.next = even_node.next
        return odd_node.next
