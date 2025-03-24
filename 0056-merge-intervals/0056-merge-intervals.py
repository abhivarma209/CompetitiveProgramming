class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        last_day = -1
        for interval in intervals:
            if interval[0]>last_day:
                res.append(interval)
                last_day = interval[1]
            else:
                res[-1][1] = max(res[-1][1],interval[1])
                last_day = max(last_day,interval[1])
        return res