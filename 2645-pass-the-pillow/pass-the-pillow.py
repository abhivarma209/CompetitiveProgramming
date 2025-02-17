class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        loops = time//(n-1)
        diff = time%(n-1)
        if loops%2 == 1:
            return n-diff
        else:
            return diff+1
        