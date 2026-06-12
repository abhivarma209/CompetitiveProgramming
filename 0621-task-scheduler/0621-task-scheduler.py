class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = dict()
        for task in tasks:
            d[task]=d.get(task,0)+1
        heap = [-f for f in d.values()]
        heapq.heapify(heap)
        q=deque()
        time=0
        while q or heap:
            time+=1
            if heap:
                count = 1+heapq.heappop(heap)
                if count<0:
                    q.append((count,time+n))
            
            if q and q[0][1]<=time:
                left = q.popleft()
                heapq.heappush(heap,left[0])
        return time