class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        res = 0
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            else:
                st.pop()
                if len(st)==0:
                    st.append(i)
                else:
                    res=max(res,i-st[-1])
        return res
