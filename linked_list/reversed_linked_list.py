class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        prev = None
        current = head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev


if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    new_head = sol.reverse_list(head)
    while new_head:
        print(new_head.val)
        new_head = new_head.next
