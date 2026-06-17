class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        graph = {i:[] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    graph[i].append(j)
        vis=set()
        def dfs(node):
            vis.add(node)
            for nei in graph[node]:
                if nei not in vis:
                    dfs(nei)
        res=0
        for node,neis in graph.items():
            if node not in vis:
                res+=1
            dfs(node)
        return res

        