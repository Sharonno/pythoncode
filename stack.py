class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.size = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue1.append(x)
        self.size += 1

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue1.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        return self[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if self:
            return False
        return True


if __name__ == '__main__':
    a = Stack()
    a.push(1)
    print a.pop()