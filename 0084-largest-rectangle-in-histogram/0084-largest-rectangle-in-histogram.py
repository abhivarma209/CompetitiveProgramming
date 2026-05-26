class Solution:
    def pse(self, arr: List[int]) ->  List[int]:
        st=[0]
        res=[-1] * (len(arr))
        for i in range(1,len(arr)):
            while len(st)>0 and arr[st[-1]]>=arr[i]:
                st.pop()
            if st and arr[st[-1]]<arr[i]:
                res[i]=st[-1]
            st.append(i)
        return res
    
    def nse(self, arr: List[int]) ->  List[int]:
        st=[]
        res=[len(arr)]*len(arr)
        for i in range(len(arr)):
            while st and arr[st[-1]]>arr[i]:
                idx=st.pop()
                res[idx]=i
            st.append(i)
        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        pse=self.pse(heights)
        nse=self.nse(heights)
        area = 0
        for i in range(len(heights)):
            height = heights[i]
            width = nse[i]-pse[i]-1
            area = max(area, height*width)
        return area