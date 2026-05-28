class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for num in asteroids:
            if not st:
                st.append(num)
            else:
                if  num>0:
                    st.append(num)
                else:
                    while st and st[-1]>0 and st[-1]<abs(num):
                        st.pop()
        
                    if not st or st[-1]<0:
                        st.append(num)
                    elif st and st[-1]==abs(num):
                        st.pop()
                    elif st and st[-1]>abs(num):
                        continue
        return st
                    
                    