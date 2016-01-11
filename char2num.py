class Solution(object):
    def convert2Title(self, n):
        ch = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''
        # cnt = 0
        
        while n > 26:
            tmp = n % 26
            result += ch[tmp-1]            
            n = n / 26
            
        if n < 27:
            if n in [1,26]:            
                result += ch[n-1]
            else:
                result += ch[n - 2]

        r = result[::-1]

        return r
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            reurn
        l = len(s)
        flag  = 0
        result = 0
        for i in s:
            result += pow(26, l-1-flag) * (ord(i) - 64)
            flag += 1
            
        return result


if __name__ == '__main__':
    a = Solution()
    num = a.titleToNumber('ABC')

    print num