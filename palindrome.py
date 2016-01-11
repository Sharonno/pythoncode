def isPalindrome(n): 
    """
    :type x: int 
    :rtype: bool
    """
    if n < 0 or n == 0:
        n = -n

    tmp = str(n)
    return palindromeHelper(tmp, len(tmp)-1, 0)

def palindromeHelper(string, high, low):
    if high <= low:
        return True
        
    elif string[high] != string[low]:
        return False
    else:
        return palindromeHelper(string, high-1, low+1)

if __name__ == '__main__':
    i = 12321
    print isPalindrome(i)