class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for token in tokens:
            if token not in ["+","-","*","/"]:
                st.append(int(token))
            else:
                t1=st.pop()
                t2=st.pop()
                if token=='+':
                    st.append(t1+t2)
                elif token=="-":
                    st.append(t2-t1)
                elif token=="*":
                    st.append(t2*t1)
                else:
                    div = t2/t1
                    div = math.floor(div) if div>0 else math.ceil(div)
                    st.append(div)
        return st[-1]
        