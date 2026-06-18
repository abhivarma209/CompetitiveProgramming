class Solution:
    def find(self,a):
        if self.parent[a]!=a:
            self.parent[a]=self.find(self.parent[a])
        return self.parent[a]

    def union(self,x,y):
        self.parent[self.find(x)]=self.find(y)
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parent = [i for i in range(len(s))]
        for a,b in pairs:
            self.union(a,b)
        
        groups = defaultdict(list)
        for i,ch in enumerate(s):
            parent = self.find(i)
            groups[parent].append(i)

        res=[''] * len(s)
        for arr in groups.values():
            chars = sorted(s[i] for i in arr)
            arr.sort()
            for idx,ch in zip(arr,chars):
                res[idx]=ch
        return ''.join(res)
