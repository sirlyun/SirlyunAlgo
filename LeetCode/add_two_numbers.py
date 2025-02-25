'''
    given two non-empty linked lists representing two non-negative integers

    The digits are stored in reverse order
    each of their nodes contains a single digit

    Add the two numbers and return the sum as a linked list
    the two numbers do not contain any leading zero, except the number 0 itself
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = int(
            self.makeListNodeToNum(
                result='',
                now_l=l1
            )
        )
        num2 = int(
            self.makeListNodeToNum(
                result='',
                now_l=l2
            )
        )
        num = num1 + num2

        str_num = str(num)
        l = None

        return self.makeNumToListNode(
            str_num=str_num,
            idx=len(str_num)-1
        )


    def makeNumToListNode(self, str_num: str, idx: int):
        if idx == 0:
            return ListNode(
                val=int(str_num[idx]),
                next=None
            )

        return ListNode(
            val=int(str_num[idx]),
            next=self.makeNumToListNode(
                str_num=str_num,
                idx=idx-1
            )
        )

    def makeListNodeToNum(self, result, now_l):
        if now_l.next is None:
            return str(now_l.val)+result

        return self.makeListNodeToNum(
            result=str(now_l.val)+result,
            now_l=now_l.next
        )