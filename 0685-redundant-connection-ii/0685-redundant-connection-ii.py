class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [1] * (n+1)
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px,py=self.find(x),self.find(y)
        if px==py: return False
        if self.size[py]>self.size[px]:
            self.size[py]+=self.size[px]
            self.parent[px]=self.parent[py]
        else:
            self.size[px]+=self.size[py]
            self.parent[py]=self.parent[px]
        return True
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        uf = UnionFind(len(edges)+1)
        edge1,edge2=None,None
        for u,v in edges:
            if v in parent:
                edge1=[parent[v],v]
                edge2=[u,v]
                break
            else:
                parent[v] = u
        for u,v in edges:
            if [u,v] == edge2:
                continue
            if not uf.union(u,v):
                return edge1 if edge1 else [u,v]
        return edge2           