# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        if not head.next:
            return head
        tmp = head
        while tmp:            
            while tmp.next and tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            tmp = tmp.next            
        return head


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(1)
    # root.next.next = ListNode(1)
    # root.next.next.next = ListNode(2)
    # root.next.next.next.next = ListNode(3)
    # root.next.next.next.next.next = ListNode(3)
    # root.next.next.next.next.next.next = ListNode(4)
    # root.next.next.next.next.next.next.next = ListNode(5)

    re = Solution().deleteDuplicates(root)
    l = []
    while re:
        l.append(re.val)
        re = re.next

    print l
