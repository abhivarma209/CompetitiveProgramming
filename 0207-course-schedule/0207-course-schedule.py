class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}
        for x,y in prerequisites:
            graph[x].append(y)
        vis = [0] * numCourses
        def dfs(node):
            vis[node]=1
            for nei in graph[node]:
                if vis[nei]==1:
                    return True
                if vis[nei]==0:
                    if dfs(nei):
                        return True
            vis[node]=2
            return False
        for k in graph.keys():
            if vis[k]==0:
                if dfs(k): return False
        return True