#-*-coding=utf-8-*-
import Queue
class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def MaxDepth(root):
    '''
    递归求最大深度
    '''
    if not root:
        return 0
    else:
        return max(MaxDepth(root.left), MaxDepth(root.right)) + 1
  
def MaxWidth(root):
    if not root:
        return 0
    q = Queue.Queue()
    q.put(root)

    curwidth = 0
    maxwidth = 0

    while not q.empty():
        curwidth = q.qsize()
        for i in range(curwidth):
            tree = q.get()
            if tree.left:
                q.put(tree.left)
            if tree.right:
                q.put(tree.right)
        if curwidth > maxwidth:
            maxwidth = curwidth
    return maxwidth
'''
import pdb
def treeWidth(tree):
    curwidth=1
    maxwidth=0
    q=Queue.Queue()
    q.put(tree)
    pdb.set_trace()
    while not q.empty():
        print q.qsize(),'sizeofqueue  '
        n=curwidth
        for i in range(n):
            tmp=q.get()
            curwidth-=1
            if tmp.left:
                q.put(tmp.left)
                curwidth+=1
            if tmp.right:
                q.put(tmp.right)
                curwidth+=1
        if curwidth>maxwidth:
            maxwidth=curwidth
    return maxwidth
'''
if __name__ == '__main__':
    root = Node('D',Node('B', Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    #wid = treeWidth(root)
    wid = MaxWidth(root)
    print wid