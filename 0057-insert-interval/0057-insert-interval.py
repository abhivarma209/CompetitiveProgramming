class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        days = intervals.copy()
        days.append(newInterval)
        days.sort()
        res = []
        last_day = -1
        for day in days:
            if day[0]>last_day:
                res.append(day)
                last_day = day[1]
            else:
                res[-1][1] = max(res[-1][1],day[1])
                last_day = max(last_day,day[1])
        return res