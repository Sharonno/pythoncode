# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preOrder(self, root):
        if not root:
            return []
        result = []
        curLayer = [root]
        while curLayer:
            node = []
            for i in range(len(curLayer)):
                tmp = curLayer.pop(0)
                node.append(tmp.val)
                if tmp.left:
                    curLayer.append(tmp.left)
                if tmp.right:
                    curLayer.append(tmp.right)
            result.append(node)
            
        # print result,'alili'    
        return result


    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        r = self.preOrder(root)
        print r
        r = r[::-1]
        print r
        # for i in range(len(r)):
        #     tmp = r[i]
        #     r[i] = r[-(i+1)]
        #     r[-(i+1)] = tmp
        #print r,'rrrrrr'


        return r
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    a = Solution()
    b = a.levelOrderBottom(root)
    print b