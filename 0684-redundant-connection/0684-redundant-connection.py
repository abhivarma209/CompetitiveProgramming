class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [1] * (n+1)

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px,py = self.find(x),self.find(y)
        if px==py: return False
        if self.size[py]>self.size[px]:
            self.parent[px]=self.parent[py]
            self.size[py]+=self.size[px]
        else:
            self.parent[py]=self.parent[px]
            self.size[px]+=self.size[py]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1)
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
        return []