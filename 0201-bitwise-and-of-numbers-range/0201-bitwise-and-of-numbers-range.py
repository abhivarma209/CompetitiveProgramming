class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left==0:
            return 0
        shift = 0
        while left>0 and right>0:
            if left==right:
                return left<<shift
            left >>= 1
            right >>= 1
            shift +=1
        return 0