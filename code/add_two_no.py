# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        no1 = 0
        index1 = 0
        no2 = 0
        index2 = 0
        while l1 is not None:
            # print(l1.val)
            no1 += l1.val * (10 ** index1)
            index1 += 1
            l1 = l1.next

        while l2 is not None:
            # print(l2.val)
            no2 += l2.val * (10 ** index2)
            index2 += 1
            l2 = l2.next

        # print(no1)
        # print(no2)
        no3 = no1 + no2
        # print(no3)
        mainNode = ListNode(0)
        prevNode = None
        main_flag = 0
        while no3 > 0:
            currentNode = ListNode(no3 % 10, None)
            if prevNode is not None:
                prevNode.next = currentNode
            if main_flag == 0:
                mainNode = currentNode
                main_flag = 1
            prevNode = currentNode
            no3 = no3 // 10
            # print(no3)

        # while mainNode is not None:
        #     print(mainNode.val)
        #     mainNode = mainNode.next
        return mainNode

def solve(x):
    while x != None:
        print(x.val)
        x = x.next


so = Solution()
n3 = ListNode(3)
n2 = ListNode(4, n3)
n1 = ListNode(2, n2)

n6 = ListNode(4)
n5 = ListNode(6, n6)
n4 = ListNode(5, n5)

# solve(n1)
n7 = ListNode(0)
n8 = ListNode(0)

sol = Solution()
solve(sol.addTwoNumbers(n1, n4))
solve(sol.addTwoNumbers(n7,n8))
