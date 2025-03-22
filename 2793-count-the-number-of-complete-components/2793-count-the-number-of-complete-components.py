class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        check = [0] * n
        res = 0
        graph = [[i] for i in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        for dfs in graph:
            dfs.sort()
        for i,dfs in enumerate(graph):
            sz = len(dfs)
            if sz == 0:
                res += 1
                continue
            if check[i] == 0:
                cycle = True
                for node in dfs:
                    if graph[node] != dfs:
                        cycle = False
                    check[node] = True
                if cycle:
                    res+=1
        return res