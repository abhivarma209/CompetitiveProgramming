class Solution:
    def calculate(self, s: str) -> int:
        st = []
        res,i=0,0
        while i<len(s):
            if s[i]==" " or s[i]=="+":
                i+=1
            elif s[i]=="(":
                st.append("(")
                i+=1
            elif s[i]==")":
                temp=0
                while st:
                    top=st.pop()
                    if top=="(":
                        break
                    elif type(top)==int:
                        if st and st[-1]=='-':
                            top*=(-1)
                            st.pop()
                        temp+=top
                if st and st[-1]=='-':
                    temp*=-1
                    st.pop()
                st.append(temp)
                i+=1
            elif '0'<=s[i]<='9':
                num=""
                while i<len(s) and '0'<=s[i]<='9':
                    num+=s[i]
                    i+=1
                num = int(num)
                if st and st[-1]=='-':
                    st.pop()
                    num*=(-1)
                st.append(num)
            elif s[i]=='-':
                st.append("-")
                i+=1
        while st:
            el = st.pop()
            if el=='-':
                res*=-1
            elif type(el)==int:
                res+=el
        return res