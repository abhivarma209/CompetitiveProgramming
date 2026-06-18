class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for ex,ey in prerequisites:
            graph[ex].append(ey)
        vis = [0] * numCourses
        order=[]
        def dfs(node):
            vis[node]=1
            for nei in graph[node]:
                if vis[nei]==1: return False
                if vis[nei]==0:
                    if not dfs(nei): return False
            vis[node]=2
            order.append(node)
            return True
        
        for course in range(numCourses):
            if vis[course]==0:
                if not dfs(course): return []
        return order


        
        
    
