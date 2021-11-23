# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q = None 
        node = head 
        vals = []
        while node is not None :
            vals.append(node.val)
            node = node.next
        
        head = None
        if len(vals) <= 0:
            return head
        val = vals.pop()
        
        while val is not None:
            
            if head is None:
                head = ListNode(val=val)
                node = head
                # print(head.val)
            else :
                
                node.next = ListNode(val=val)
                node = node.next
            
            if len(vals) > 0 :
                val = vals.pop()
            else: val = None        
        return head