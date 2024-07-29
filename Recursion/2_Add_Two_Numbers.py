# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next: ListNode
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def read_val(node: ListNode):
            if node.next == None:
                return node.val
            return node.val + read_val(node.next) * 10

        def write_val(n):
            if n == 0:
                return None
            return ListNode(n % 10, write_val(n//10))

        sum_two = read_val(l1) + read_val(l2)
        final = write_val(sum_two) if sum_two != 0 else ListNode(0, None)
        
        return final
        