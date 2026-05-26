class Solution:
    def simplifyPath(self, path: str) -> str:
        i,j=0,0
        stack = []
        while i<len(path) and j<len(path):
            i=j
            while i<len(path) and path[i]=='/':
                i+=1
            j=i
            while j<len(path) and path[j]!='/':
                j+=1
            folder = path[i:j]
            if folder=='..':
                if len(stack)>0:
                    stack.pop()
            elif folder in ['.','']:
                continue
            else:
                stack.append(folder)
        if len(stack)==0: return "/"
        res=""
        for folder in stack:
            res+='/'
            res+=folder
        return res

