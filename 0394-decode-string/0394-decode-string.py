class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        res=""
        for i,ch in enumerate(s):
            if not st:
                if '0'<=ch<='9':
                    st.append(int(ch))
                else: st.append(ch)
                continue
            if '0'<=ch<='9':
                if st and type(st[-1])==int:
                    curr=st.pop()*10+int(ch)
                    st.append(curr)
                else:
                    st.append(int(ch))
            elif 'a'<=ch<='z':
                if i>=1 and 'a'<=s[i-1]<='z':
                    curr=st.pop()+ch
                    st.append(curr)
                else:
                    st.append(ch)
            elif ch=='[':
                st.append('[')
            elif ch==']':
                curr=""
                while st and st[-1]!='[':
                    temp = st.pop()
                    if type(st[-1])==int:
                        temp = temp * st.pop()
                    curr=temp+curr
                st.pop()
                st.append(curr)
            
        num = 1
        for ch in st:
            if type(ch)==int:
                num=ch
            else:
                temp = ch * num
                res+=temp
                num=1
        return res
            

            
            


    