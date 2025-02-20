class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        while len(arr)>0:
            temp = arr[0]
            arr.remove(temp)
            if temp>0:
                if temp*2 not in arr:
                    return False
                arr.remove(temp*2)
            else:
                if temp//2 not in arr:
                    return False
                if (temp//2)*2 != temp:
                    return False
                arr.remove(temp//2)
            
        return True
        