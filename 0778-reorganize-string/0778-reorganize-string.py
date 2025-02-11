class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0]*26
        last_updated = ''
        res = ""
        for ch in s:
            freq[ord(ch)-ord('a')]+=1

        max_val = max(freq)
        max_idx = freq.index(max_val)
        prev_idx = max_idx
        freq[max_idx]-= 1
        res+=chr(ord('a')+max_idx)

        flag = True
        while flag:
            left_list = freq[:prev_idx]
            right_list = freq[prev_idx+1:] if prev_idx+1 < 26 else []
            left_val = max(left_list) if len(left_list) > 0 else 0
            right_val = max(right_list) if len(right_list) > 0 else 0
            max_val = max(left_val,right_val)
            max_idx = 26
            for idx,val in enumerate(freq):
                if(idx==prev_idx):
                    continue
                if val == max_val:
                    max_idx = idx
                    prev_idx = max_idx
                    break
            if max_val == 0 or max_idx == 26:
                break
            freq[max_idx]-=1
            res+=chr(ord('a')+max_idx)
        
        if len(s) != len(res):
            return ""

        return res
