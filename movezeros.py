class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #print len(nums)
        for i in nums:
            print i,val
            if i == val:
                nums.remove(i)
                print nums , len(nums)
            # else:
            #     continue
        ll = len(nums)
        #print ll
        return ll
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
            else:
                continue

if __name__ == '__main__':
    l= [3,3,4,3,4]
    a=Solution()
    ll = a.removeElement(l, 3)
    