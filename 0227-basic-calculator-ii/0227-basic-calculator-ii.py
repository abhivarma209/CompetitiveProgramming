class Solution:
    def calculate(self, s: str) -> int:
        st=[]
        i,res=0,0
        while i<len(s):
            if '0'<=s[i]<='9':
                curr=0
                while i<len(s) and '0'<=s[i]<='9':
                    curr=curr*10+int(s[i])
                    i+=1
                if st and st[-1] in ['*','/']:
                    sign = st.pop()
                    if sign == '*':
                        curr*=st.pop()
                    else:
                        div=st.pop()/curr
                        curr=math.ceil(div) if div<0 else math.floor(div)
                elif st and st[-1]=='-':
                    curr*=(-1)
                    st.pop()
                st.append(curr)
            elif s[i] in ['*','/','-']:
                st.append(s[i])
                i+=1
            else:
                i+=1
        res=0
        for num in st:
            res+=num
        return res