class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        s_len = len(s)
        sub_str = s[0:k]
        if sub_str.count(sub_str[0]) == k:
            if s_len == k or sub_str[k-1] != s[k]:
                return True

        for i in range(1,s_len-k+1):
            sub_str = s[i:i+k]
            if sub_str.count(sub_str[0]) == k:
                if s[i-1] != sub_str[0]:
                    if i+k<s_len and s[i+k] != sub_str[k-1]:
                        return True
                    if i+k == s_len:
                        return True
        
        return False