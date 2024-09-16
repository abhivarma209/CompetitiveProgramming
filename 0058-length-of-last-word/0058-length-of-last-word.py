class Solution(object):
    def lengthOfLastWord(self, s):
        res=0
        s=s[::-1].strip()
        for x in s:
            if(x==' '): break
            else: res+=1
        
        return res
        """
        :type s: str
        :rtype: int
        """
        