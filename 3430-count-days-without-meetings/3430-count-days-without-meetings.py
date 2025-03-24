class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        i,res = 0,0
        last_day = 0
        for i in range(len(meetings)):
            if meetings[i][0]>last_day:
                res += meetings[i][0]-1-last_day
            last_day = max(last_day,meetings[i][1])
        res += days-last_day
        return res