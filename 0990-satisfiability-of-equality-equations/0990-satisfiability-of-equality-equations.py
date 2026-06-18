class UnionFind():
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
            self.size[py]+=self.size[px]
            self.parent[px]=self.parent[py]
        else:
            self.size[py]+=self.size[px]
            self.parent[px]=self.parent[py]
        return True
    
    def connected(self,x,y):
        return self.find(x)==self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        ascii_a = ord('a')
        for equation in equations:
            val1,val2=ord(equation[0])-ascii_a,ord(equation[-1])-ascii_a
            if equation[1]=='=':
                uf.union(val1,val2)
        for equation in equations:
            val1,val2=ord(equation[0])-ascii_a,ord(equation[-1])-ascii_a
            if equation[1]=='!':
                if uf.connected(val1,val2):
                    return False
        return True
