class Solution:
    def recursive(self,char_count):
        res = 0
        for i in range(26):
            if char_count[i]>0:
                res += 1
                char_count[i] -= 1
                res += self.recursive(char_count)
                char_count[i] += 1

        return res


    def numTilePossibilities(self, tiles: str) -> int:
        char_count = [0] * 26
        for tile in tiles:
            char_count[ord(tile)-ord('A')]+=1

        return self.recursive(char_count)
        
        