
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node_1 = head
        cur_node_2 = head.next if head else None
        pre_node = None
        result = cur_node_2 if cur_node_2 and cur_node_1 else cur_node_1
        while True:
            if cur_node_1 and cur_node_2:
                if pre_node:
                    last = cur_node_2.next
                    cur_node_1.next = last
                    cur_node_2.next = cur_node_1
                    pre_node.next = cur_node_2
                else:
                    last = cur_node_2.next
                    cur_node_1.next = last
                    cur_node_2.next = cur_node_1                    
            else:
                break
            pre_node = cur_node_1
            cur_node_1 = cur_node_1.next if cur_node_1 else None
            cur_node_2 = cur_node_1.next if cur_node_1 else None
        return result

if __name__ == "__main__":
    sl = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    result = sl.swapPairs(l1)
    while True:
        print(result.val)
        result = result.next
        if not result.next:
            print(result.val)
            break
    print(result)
