from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cin_stack = list()
        pa = l1
        pb = l2
        result = ListNode(0)
        result_head = result
        while True:
            if cin_stack:
                cin = cin_stack.pop()
            else:
                cin = 0
            if not pa and not pb:
                if cin != 0:
                    result.next = ListNode(cin)
                else:
                    break
            else:
                a_val = pa.val if pa else 0
                b_val = pb.val if pb else 0
                if cin + a_val + b_val >= 10:
                    cin_stack.append(1)
                    result.next = ListNode(cin+a_val+b_val-10)
                else:
                    result.next = ListNode(cin+a_val+b_val)

            pa = pa.next if pa else None
            pb = pb.next if pb else None
            result = result.next
        return result_head.next

if __name__ == "__main__":
    sl = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    result = sl.addTwoNumbers(l1, l2)
    while True:
        print(result.val)
        result = result.next
        if not result.next:
            print(result.val)
            break
    print(result)