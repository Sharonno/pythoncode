def isUgly(n):
    if n <= 0:
        return 0

    p_2 = 0
    p_3 = 0
    p_5 = 0

    UglyNums = [0] * n
    UglyNums[0] = 1
    nextIndex = 1

    while nextIndex < n:
        num_min = min(UglyNums[p_2]*2, UglyNums[p_3]*3, UglyNums[p_5]*5)
        UglyNums[nextIndex] = num_min

        while UglyNums[p_2]*2 <= UglyNums[nextIndex]:
            p_2 += 1

        while UglyNums[p_3]*3 <= UglyNums[nextIndex]:
            p_3 += 1

        while UglyNums[p_5] *5 <= UglyNums[nextIndex]:
            p_5 += 1

        nextIndex += 1

    return UglyNums[nextIndex - 1]


if __name__ == '__main__':
    n = 2
    print isUgly(n)