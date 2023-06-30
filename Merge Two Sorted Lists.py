# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:

    @staticmethod
    def get_sorted_lists(list1: ListNode, list2: ListNode):
        if list1 and list1.val <= list2.val:
            return list1, list2
        return list2, list1

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        list1, list2 = self.get_sorted_lists(list1, list2)
        merged_list_head = list1
        current_node = list1
        list1 = list1.next
        while list1.val and list2.val:
            list1, list2 = self.get_sorted_lists(list1, list2)
            current_node.next = list1
            current_node = list1
            list1 = list1.next
        if list1.val is None:
            current_node.next = list2
        else:
            current_node.next = list1
        return merged_list_head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next
