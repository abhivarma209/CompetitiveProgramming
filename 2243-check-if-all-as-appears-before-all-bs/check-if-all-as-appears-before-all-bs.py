class Solution:
    def checkString(self, s: str) -> bool:
        b_check = False
        for ch in s:
            if ch == 'b':
                b_check = True
            else:
                if b_check:
                    return False
        return True