class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q=deque([])
        q.append((startGene,0))
        res=len(bank)+2
        words=set(bank)
        vis = set()
        while q:
            word,count=q.popleft()
            if word==endGene: res=min(res,count)
            for i in range(len(word)):
                for j in ['A', 'C', 'G', 'T']:
                    nw=word[:i]+j
                    if i<len(word)-1:
                        nw+=word[i+1:]
                    if nw not in words or nw in vis: continue
                    q.append((nw,count+1))
                    vis.add(nw)
        return -1 if res==len(bank)+2 else res
        