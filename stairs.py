class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        n += 1
        phi = pow(5, 0.5) + 1
        phi /= 2
        fn = pow(phi, n) - pow(-phi,-n)
        fn /= pow(5, 0.5)

        return fn


if __name__ == '__main__':
    print Solution().climbStairs(5)