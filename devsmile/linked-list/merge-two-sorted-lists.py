# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node_1 = l1
        node_2 = l2
        q = None
        
        if node_1 is None and node_2 is None:
            return None
        elif node_1 is None and node_2 is not None:
            return node_2
        elif node_1 is not None and node_2 is None:
            return  node_1
        elif node_1 is not None and node_2 is not None:
            if node_1.val < node_2.val :
                q = ListNode(val=node_1.val)
                node_1 = node_1.next
            else :
                q = ListNode(val=node_2.val)
                node_2 = node_2.next
        
        head = q
        
        while node_1 is not None or node_2 is not None:
            if node_1 is not None and node_2 is None:
                q.next = ListNode(val=node_1.val)
                q = q.next
                node_1 = node_1.next
            elif node_2 is not None and node_1 is None:
                q.next = ListNode(val=node_2.val)
                q = q.next
                node_2 = node_2.next                
            elif node_1.val <= node_2.val:
                q.next = ListNode(val=node_1.val)
                q = q.next
                node_1 = node_1.next
            elif node_2.val < node_1.val:
                q.next = ListNode(val=node_2.val)
                q = q.next
                node_2 = node_2.next
        return head
