# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, oldHead: Optional[ListNode]) -> Optional[ListNode]:
        if oldHead is None or oldHead.next is None:
            return oldHead

        newRest = self.swapPairs(oldHead.next.next)
        newHead = oldHead.next
        newHead.next = oldHead
        oldHead.next = newRest
        return newHead