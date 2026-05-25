class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        for i in range(len(s)):
            if s[i]=='(':
                st.append('(')
            else:
                if len(st)==0 or st[-1]==')':
                    st.append(')')
                else:
                    st.pop()
        return len(st)