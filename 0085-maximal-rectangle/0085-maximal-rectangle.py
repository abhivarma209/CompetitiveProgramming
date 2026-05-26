class Solution:
    def pse(self, arr:List[int]) -> List[int]:
        res=[-1]*(len(arr))
        st=[]
        for i in range(len(arr)):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            if st and arr[st[-1]]<arr[i]:
                res[i]=st[-1]
            st.append(i)
        return res

    def nse(self, arr:List[int]) -> List[int]:
        res=[len(arr)]*(len(arr))
        st=[]
        for i in range(len(arr)):
            while st and arr[st[-1]]>arr[i]:
                res[st[-1]]=i
                st.pop()
            st.append(i)
        return res
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        histogram = []
        area = 0
        for i in range(0,len(matrix)):
            histogram.append([])
            if i==0:
                for bi in matrix[0]:
                    histogram[0].append(int(bi))
                continue
            for j in range(len(matrix[0])):
                if int(matrix[i][j])==1:
                    histogram[i].append(histogram[i-1][j]+1)
                else:
                    histogram[i].append(0)
        for arr in histogram:
            nse=self.nse(arr)
            pse=self.pse(arr)
            for i in range(len(arr)):
                height=arr[i]
                width=nse[i]-pse[i]-1
                area = max(area,width*height)
        return area