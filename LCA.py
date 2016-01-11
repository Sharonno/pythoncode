#-*-coding=utf-8-*-
import Queue
class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

class Solution:
  # @param {Node} root
  # @param {Node} p
  # @param {Node} q
  # @return {Node}
  def lowestCommonAncestor(self, root, p, q):
    if not root:
        return None
    if root in [p,q]:
        return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)


    if left and right:
        return root
    if left:
        return left
    if right:
        return right
    return None
    
if __name__ == '__main__':
    root = Node(3,Node(5, Node(6),Node(2, Node(7), Node(4))),Node(1,Node(0),Node(8)))
    r = Node(3,Node(5),Node(1))
    a = Solution()
    b = a.lowestCommonAncestor(r, Node(5),Node(1))
    print b