class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_map = {}
        left,res = 0,0
        n = len(s)
        for right in range(n):
            char_map[s[right]] = char_map.get(s[right],0) + 1
            while len(char_map) == 3:
                res += n-right
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    del char_map[s[left]]
                left += 1
        return res
        