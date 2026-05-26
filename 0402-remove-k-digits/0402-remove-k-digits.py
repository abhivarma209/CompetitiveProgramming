class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[-1]
        for i in range(len(num)):
            n=int(num[i])
            if n>=st[-1]:
                st.append(n)
            else:
                while k>0 and len(st)>1 and n<st[-1]:
                    st.pop()
                    k-=1
                st.append(n)
        res=""
        for i in range(1,len(st)-k):
            if len(res)==0 and st[i]==0:
                continue
            res+=str(st[i])
        if len(res)==0: res+="0"
        return res