class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        n = len(arr)
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                first = arr[i]
                second = arr[j]
                find = first + second
                temp = 2
                while find in nums:
                    first = second
                    second = find
                    find = first + second
                    temp += 1
                if temp>2: res = max(temp,res)
        return res