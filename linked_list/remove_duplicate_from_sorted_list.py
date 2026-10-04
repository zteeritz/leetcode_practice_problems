class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


if __name__ == '__main__':
    sol = Solution()
    # head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    head = ListNode(1, ListNode(1, ListNode(2)))
    new_head = sol.delete_duplicates(head)
    while new_head:
        print(new_head.val)
        new_head = new_head.next
