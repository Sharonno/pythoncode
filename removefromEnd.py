#-*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pAhead = head
        pBehind = head
        #要删除倒数第N个节点，所以要找到倒数第N-1个节点，所以两个指针之间的距离要保持为N而不是N-1
        for i in range(n):
            pAhead = pAhead.next
        if not pAhead :
            print 'pAhead is None'
            head = head.next
            return head
        else:
            print pAhead.val

        while pAhead.next != None:
            pAhead = pAhead.next
            pBehind = pBehind.next

        print pAhead.val,'lalala'
        print pBehind.val,'okokok'
            
        pBehind.next = pBehind.next.next
        return head

if __name__ == '__main__':
    root = ListNode(0)
    root.next = ListNode(1)
    root.next.next = ListNode(2)
    # root.next.next.next = ListNode(3)
    # root.next.next.next.next = ListNode(4)
    # root.next.next.next.next.next = ListNode(5)
    a = Solution()
    re = a.removeNthFromEnd(root, 3)
    l = []
    while re != None:
        l.append(re.val)
        re = re.next

    print l


        