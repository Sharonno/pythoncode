class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
            
        if not root.left and not root.right and root.val == sum:
            return True
        
        
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        import pdb 
        pdb.set_trace()
        if not root:
            return []
        result = []
        self.findPathSum(root, sum, [], result)
        return result
    def findPathSum(self, root, sum, temp, output):
        if not root:
            return

        if not root.left and not root.right and sum == root.val:
            temp.append(root.val)
            #output.append(temp[:])
            output.append(temp)
            return

        # sum -= root.val
        # temp.append(root.val)
        self.findPathSum(root.left, sum-root.val, temp+[root.val], output)
        self.findPathSum(root.right, sum-root.val, temp+[root.val], output)
            



if __name__ == '__main__':
    root = TreeNode(1)
    ltree = TreeNode(2)
    rtree = TreeNode(3)
    root.left = ltree
    root.right = rtree
    ltree.right = TreeNode(5)
    a = Solution()
    #b = a.pathSum(root,8)
    b = a.hasPathSum(root, 8)
    print b