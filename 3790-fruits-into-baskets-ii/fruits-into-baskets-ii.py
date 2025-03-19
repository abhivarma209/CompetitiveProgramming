class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        res = 0
        for i in range(n):
            m = len(baskets)
            temp = -1
            for j in range(m):
                if baskets[j] >= fruits[i]:
                    temp = j
                    break
            if temp != -1:
                baskets.remove(baskets[temp])
            else:
                res += 1
        return res