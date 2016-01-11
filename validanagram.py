class Solution(object):
   
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if not (s or t):
            return True
        if len(s) != len(t):
            return False
        else:
            for i in set(s):
                if s.count(i) != t.count(i):
                    return False
            return True
    