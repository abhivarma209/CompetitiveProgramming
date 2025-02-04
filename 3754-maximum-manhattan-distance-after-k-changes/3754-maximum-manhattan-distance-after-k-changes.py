class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        north = 0
        south = 0
        east = 0
        west = 0
        res = 0
        for ch in s:
            if ch == 'N':
                north+=1
            elif ch == 'S':
                south+=1
            elif ch == 'E':
                east+=1
            else:
                west+=1

            v_max = max(north,south)
            v_min = min(north,south)
            h_max = max(east,west)
            h_min = min(east,west)

            temp = v_max + h_max
            min_dis = v_min + h_min
            
            if k>=min_dis: temp+=min_dis
            else: temp+= 2*k-min_dis

            res = max(res,temp)

        return res

        