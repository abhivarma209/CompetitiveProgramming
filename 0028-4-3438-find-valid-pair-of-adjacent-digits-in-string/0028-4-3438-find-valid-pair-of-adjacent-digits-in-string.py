class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        digit_list = [0] * 10
        for ch in s:
            digit_list[int(ch)]+=1

        for i,ch in enumerate(s):
            if i<len(s)-1 :
                if ch!=s[i+1] and digit_list[int(ch)] == int(ch) and digit_list[int(s[i+1])] == int(s[i+1]):
                    return s[i:i+2]
        
        return ""

        