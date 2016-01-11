# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getListLength(self, head):
        '''
        :type head: ListNode
        :rtype int
        '''
        l = 0
        tmp = head
        while tmp:
            l += 1
            tmp = tmp.next
        return l

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = self.getListLength(headA)
        l2 = self.getListLength(headB)
        l_diff = l1 - l2
        print l1,l2,l_diff

        head_long = headA
        head_short = headB

        if l2 > l1:
            head_long = headB
            head_short = headA
            l_diff = l2 - l1

        for i in xrange(l_diff):
            head_long = head_long.next

        while head_long and head_short and head_long.val != head_short.val:
            print head_long.val,head_short.val
            head_long = head_long.next
            head_short  = head_short.next
        
        common = head_long
        return common

if __name__ == '__main__':
    headA = ListNode('a1')
    headB = ListNode('b1')
    headA.next = ListNode('a2')
    headB.next = ListNode('b2')
    headB.next.next = ListNode('b3')
    headA.next.next = ListNode('c1')
    headB.next.next.next = ListNode('c1')
    headA.next.next.next = ListNode('c2')
    headB.next.next.next.next = ListNode('c2')
    headB.next.next.next.next.next = ListNode('c3')
    headA.next.next.next.next = ListNode('c3')

    print Solution().getIntersectionNode(headA,headB).val

