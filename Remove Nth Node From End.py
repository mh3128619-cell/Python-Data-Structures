class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        head = reverse(head)

        if n == 1:
            head = head.next
        else:
            curr = head
            for _ in range(n - 2):
                curr = curr.next
            curr.next = curr.next.next

        return reverse(head)
