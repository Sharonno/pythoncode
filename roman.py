class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map_dic = {"I":1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M": 1000}
        nums = [map_dic[i] for i in x]
        result = sum(nums)

        return result

if __name__ == '__main__':
    a = Solution()
    print a.romanToInt("IV")
