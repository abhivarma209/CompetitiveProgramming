class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d,res,ans={},float('inf'),[]
        for i, word in enumerate(list1):
            d[word]=i
        for i,word in enumerate(list2):
            if word in d:
                if d[word]+i<res:
                    ans = [word]
                    res=d[word]+i
                elif d[word]+i==res:
                    ans.append(word)
        return ans