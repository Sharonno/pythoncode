def isHappy(n):
    if n<= 0:
        return False
    dic = {}

    while n != 1:
        if n in dic:
            return False
        else:
            dic[n] = True
        n = sum([int(i)*int(i) for i in str(n)])
    return True

if __name__ == '__main__':
    print isHappy(19)