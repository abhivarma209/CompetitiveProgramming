class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res,last_sec = 0,-1
        for time in timeSeries:
            if time>last_sec:
                res += duration
            else:
                res += time+duration-1-last_sec
            last_sec = time+duration-1
        return res