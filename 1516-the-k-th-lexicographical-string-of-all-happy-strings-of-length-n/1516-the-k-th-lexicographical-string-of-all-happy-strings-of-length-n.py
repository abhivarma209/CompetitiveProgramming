class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        n1 = ['a','b','c']
        arr = n1
        for i in range(n):
            if i == 0:
                continue
            temp = []
            for ch in arr:
                for cn in n1:
                    if ch[-1] == cn:
                        continue
                    temp.append(ch+cn)
            arr = temp
        if len(arr)>=k:
            return arr[k-1]
        return ''