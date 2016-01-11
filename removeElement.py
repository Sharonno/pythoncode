# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        '''
        use dummy head
        '''
        if not head:
            return
        dummy = ListNode(-1)
        dummy.next = head

        pre = dummy
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummy.next
            
        
if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)

    a = Solution()
    l = a.removeElements(root,3)

    print l.val
