class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part_len = len(part)
        while True:
            idx = s.find(part)
            if idx == -1:
                return s
            left_str = s[0:idx]
            right_str = s[idx+part_len:] if idx+part_len<len(s) else ""
            s=left_str+right_str
        return ''

        