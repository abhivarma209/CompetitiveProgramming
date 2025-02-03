class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = [0] * 26
        for ch in s:
            freq[ord(ch)-ord('a')]+=1

        odd_max=1
        odd_min= sys.maxint
        even_min= sys.maxint
        even_max=1

        for num in freq:
            if num == 0:
                continue
            if num%2==1:
                odd_max = max(odd_max,num)
                odd_min = min(odd_min,num)
            else:
                even_max = max(even_max,num)
                even_min = min(even_min,num)

        return max(odd_max-even_min,odd_min-even_max)
        