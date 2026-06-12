class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        res=""
        for ch in s:
            d[ch] = d.get(ch,0)+1
        sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse = True))
        for k,v in sorted_d.items():
            temp= k*v
            res+=temp
        return res