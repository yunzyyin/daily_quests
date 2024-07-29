# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_order = []

        def read_next_node(node: ListNode):
            if node:
                node_order.append(node)
                read_next_node(node.next)

        read_next_node(head)

        while len(node_order) >= 2:
            node_order.pop(0).next = node_order[-1]
            if len(node_order) >= 2:
                node_order.pop(-1).next = node_order[0]

        node_order.pop().next = None
