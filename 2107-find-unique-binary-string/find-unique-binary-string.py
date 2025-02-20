class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        dig = ["0","1"]
        n = len(nums)
        arr = dig

        for i in range(n):
            if i == 0:
                continue
            temp = []
            for st in arr:
                temp.append(st+"0")
                temp.append(st+"1")
            arr = temp
        
        for st in arr:
            if st not in nums:
                return st
        return ""
        