from typing import Optional


class ListNode:
    pass


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        atual = dummyHead
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            colunaSoma = l1Val + l2Val + carry
            carry = colunaSoma // 10
            novoNode = ListNode(colunaSoma % 10)
            atual.next = novoNode
            atual = novoNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next

if __name__ == '__main__':
    print(Solution().addTwoNumbers(l1=[2,4,3], l2=[5,6,4]))