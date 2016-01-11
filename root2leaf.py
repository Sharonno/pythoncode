class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        import pdb
        pdb.set_trace()
        if not root:
            return []

        if not root.left and not root.right:
            print root.val,'rootval'
            return [str(root.val)]

        path = [str(root.val) + p for p in self.binaryTreePaths(root.left)]
        print path,
        path += [str(root.val) + p for p in self.binaryTreePaths(root.right)]
        print path,'sss'

        return path
        # return ['{}->{}'.format(root.val, p) 
        #         for subtree in (root.left, root.right) if subtree
        #         for p in self.binaryTreePaths(subtree)]
    
if __name__ == '__main__':
    root = TreeNode('1')
    ltree = TreeNode('2')
    rtree = TreeNode('3')
    root.left = ltree
    root.right = rtree
    ltree.right = TreeNode('5')
    a = Solution()
    b = a.binaryTreePaths(root)
    #print b



