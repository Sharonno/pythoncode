global size
def search(row):
    '''
    :num: int 
    :rtype: 
    '''
    if row == size:
        return True

def isValid(self, row, col):
    for i in range(1, row + 1):
        if self.queens[row - i] in [col, col + i, col - i]:
            return False
    return True



if __name__ == '__main__':
    size = 8
    queens = [-1] * size


