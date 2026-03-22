class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        for ch in s:
            if ch in set(['(','{','[']):
                seen.append(ch)
            else:
                if len(seen)==0:
                    return False
                if ch == ')':
                    if seen[-1] == '(':
                        seen.pop()
                    else:
                        return False
                elif ch == '}':
                    if seen[-1] == '{':
                        seen.pop()
                    else:
                        return False
                if ch == ']':
                    if seen[-1] == '[':
                        seen.pop()
                    else:
                        return False
        return True if len(seen) == 0 else False
                
        