class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st=[]
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            elif s[i]==')':
                if len(st)==0 or s[st[-1]]==')':
                    st.append(i)
                else:
                    st.pop()
        j,res=0,""
        for i in range(len(s)):
            if j<len(st) and i==st[j]:
                j+=1
            else:
                res+=s[i]
        return res
