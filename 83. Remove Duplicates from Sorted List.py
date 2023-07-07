# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        items = set()
        items.add(head.val)
        head_to_return = head
        item = head.next
        tmp_node = head
        while item:
            if item.val in items:
                item = item.next
                tmp_node.next = None
            else:
                items.add(item.val)
                tmp_node.next = item
                tmp_node = item
        return head_to_return

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr = head

        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head


l3 = ListNode(3)
l2 = ListNode(1, l3)
l1 = ListNode(1, l2)

obj = Solution()
print(obj.deleteDuplicates(l1))
