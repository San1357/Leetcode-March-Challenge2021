'''Problem : Swapping Nodes in A Linked Lists '''

#CODE :


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        A, B = head, head
        for i in range(1, k): A = A.next
        nodeK, A = A, A.next
        while A: A, B = A.next, B.next
        nodeK.val, B.val = B.val, nodeK.val
        return head
