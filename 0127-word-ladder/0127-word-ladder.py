class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q=deque([])
        q.append((beginWord,1))
        res=len(wordList)+2
        words=set(wordList)
        vis = set()
        while q:
            word,count=q.popleft()
            if word==endWord: res=min(res,count)
            for i in range(len(word)):
                for j in range(26):
                    al = chr(ord('a')+j)
                    nw=word[:i]+al
                    if i<len(word)-1:
                        nw+=word[i+1:]
                    if nw not in words or nw in vis: continue
                    q.append((nw,count+1))
                    vis.add(nw)
        return 0 if res==len(wordList)+2 else res

                