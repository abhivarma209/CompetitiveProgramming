class Solution:
    def maximumTime(self, time: str) -> str:
        res = ''
        if time[0] == '?':
            if time[1] in ['0','1','2','3','?']:
                res += '2'
            else:
                res += '1'
        else:
            res += time[0]
        if time[1] == '?':
            if res[0] == '2':
                res += '3'
            else:
                res += '9'
        else:
            res += time[1]
        res += ':'
        if time[3] == '?':
            res += '5'
        else:
            res += time[3]
        if time[4] == '?':
            res += '9'
        else:
            res += time[4]
        return res
        