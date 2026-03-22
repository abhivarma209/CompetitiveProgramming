class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        os = set(['(','{','['])
        for ch in s:
            if ch in os:
                seen.append(ch)
            else:
                if len(seen)==0:
                    return False
                last = seen.pop()
                if ch==')' and last != '(': return False
                if ch==']' and last != '[': return False
                if ch=='}' and last != '{': return False
        return True if len(seen) == 0 else False
                
        