# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        visited = set()
        visited.add(head)
        next_node: Optional[ListNode] = head.next
        while next_node:
            if next_node.next in visited:
                return True
            visited.add(next_node)
            next_node = next_node.next
        return False


