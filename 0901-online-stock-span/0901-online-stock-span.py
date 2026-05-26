class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 0

    def next(self, price: int) -> int:
        self.day+=1
        while self.stack and self.stack[-1][0]<=price:
            self.stack.pop()
        if len(self.stack)==0:
            self.stack.append((price,self.day))
            return self.day
        top = self.stack[-1]
        if self.stack and top[0]>price:
            self.stack.append((price,self.day))
            return self.day-top[1]
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)