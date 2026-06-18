class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        vis = [0]*len(graph)
        def is_cycle(node):
            vis[node]=1
            for nei in graph[node]:
                if vis[nei]==1:
                    return True
                if vis[nei]==0:
                    if is_cycle(nei):
                        return True
            vis[node]=2
            return False
        res=[]
        for i in range(len(graph)):
            if not is_cycle(i):
                res.append(i)
        return res