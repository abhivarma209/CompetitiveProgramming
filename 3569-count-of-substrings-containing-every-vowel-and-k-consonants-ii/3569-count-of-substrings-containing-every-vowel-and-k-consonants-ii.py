class Solution:
    def isVowel(self,c):
        return c in {'a','e','i','o','u'}
    
    def atLeastK(self,word,k):
        n = len(word)
        res = 0
        con = 0
        vowel_map = {}
        left = 0

        for right in range(n):
            if self.isVowel(word[right]):
                vowel_map[word[right]] = vowel_map.get(word[right],0)+1
            else:
                con += 1
            while len(vowel_map) == 5 and con >= k:
                res += n - right
                if self.isVowel(word[left]):
                    vowel_map[word[left]] -= 1
                    if vowel_map[word[left]] == 0:
                        del vowel_map[word[left]]
                else:
                    con -= 1
                left += 1

        return res

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.atLeastK(word,k) - self.atLeastK(word,k+1)