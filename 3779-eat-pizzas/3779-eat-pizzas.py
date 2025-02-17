class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        days = len(pizzas)//4
        odd_days = days//2 + days%2
        even_days = days//2
        odd = pizzas[-odd_days:]
        even =  list(reversed(pizzas[:-odd_days]))
        res = sum(odd)
        i=1
        while even_days:
            res+=even[i]
            i+=2
            even_days-=1
        return res

        