# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        next_sum = 0
        tail = None
        head = None
        while l1 is not None  or l2 is not None :
            
            if l1 is not None and l2 is not None:
                sum_number = l1.val + l2.val + next_sum
                l1 = l1.next
                l2 = l2.next
            
            elif l1 is not None:
                sum_number = l1.val +  next_sum
                l1 = l1.next
            
            elif l2 is not None:
                sum_number = l2.val +  next_sum
                l2 = l2.next
            
            next_sum = sum_number//10

                head = ListNode(val=sum_number % 10)
                tail = head
            else:
                tail.next = ListNode(val=sum_number % 10)
                tail = tail.next

        if next_sum != 0 :
            tail.next = ListNode(val=next_sum)
            tail = tail.next
                
                
        return head