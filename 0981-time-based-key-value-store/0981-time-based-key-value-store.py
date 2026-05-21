class TimeMap:

    def __init__(self):
        self.store ={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append((timestamp,value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        vals=self.store[key]
        lo,hi=0,len(vals)-1
        res = ""
        while lo<=hi:
            mid = (hi+lo)//2
            if vals[mid][0]<=timestamp:
                res=vals[mid][1]
                lo=mid+1
            else:
                hi=mid-1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)