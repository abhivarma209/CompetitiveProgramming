class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        arr=s.split(' ')
        return len(arr[-1])
        """
        :type s: str
        :rtype: int
        """
        