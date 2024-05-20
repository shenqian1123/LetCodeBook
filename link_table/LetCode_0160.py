from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA
        curB = headB
        lenA = self.get_chain_length(headA)
        lenB = self.get_chain_length(headB)
        if lenA < lenB:
            for i in range(lenB - lenA):
                curB = curB.next
        else:
            for i in range(lenA - lenB):
                curA = curA.next
        while True:
            if not curA:
                break
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None

    def get_chain_length(self, cur: ListNode):
        result = 0
        while True:
            if not cur:
                break
            cur = cur.next
            result = result + 1

        return result

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB
        while True:
            if pA == pB and pA:
                return pA
            if not pA:
                pA = headB
            if not pB:
                pB = headA
            else:
                return None


if __name__ == "__main__":
    sl = Solution()
    con_table = ListNode(2, ListNode(4))
    l1 = ListNode(1)
    l1.next = ListNode(9)
    l1.next.next = ListNode(1)
    l1.next.next.next = con_table
    l2 = ListNode(3)
    l2.next = con_table
    # l2.next.next = ListNode(4)
    result = sl.getIntersectionNode(l1, l2)
    while True:
        print(result.val)
        result = result.next
        if not result.next:
            print(result.val)
            break
    print(result)
