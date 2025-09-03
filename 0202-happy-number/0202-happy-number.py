class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        squares = [i**2 for i in range(0,10)]
        while True:
            temp = 0
            while n>0:
                temp+=squares[n%10]
                n=n//10
            if temp in seen:
                return False
            if temp==1 or temp==7:
                return True
            n=temp
            seen.add(n)
        return False
            