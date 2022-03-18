#https://leetcode.com/problems/add-two-numbers

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'(val: {self.val}, next: {self.next})'


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    current_node = ListNode()
    first_node = current_node
    to_add = 0
    skip_l2 = False
    skip_l1 = False
    while True:
        l2_val = 0 if skip_l2 else l2.val
        l1_val = 0 if skip_l1 else l1.val
        res = l1_val + l2_val + to_add
        if to_add:
            to_add = 0
        if res >= 10:
            current_node.val = res % 10
            to_add = res // 10
        else:
            current_node.val = res

        if l1.next:
            l1 = l1.next
        else:
            skip_l1 = True

        if l2.next:
            l2 = l2.next
        else:
            skip_l2 = True

        if skip_l1 and skip_l2:
            if to_add:
                next_node = ListNode(to_add)
                current_node.next = next_node
            break

        next_node = ListNode()
        current_node.next = next_node
        current_node = next_node

    return first_node



# l1 = ListNode(9,ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
# l2 = ListNode(9,ListNode(9, ListNode(9, ListNode(9))))

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))


addTwoNumbers(l1, l2)