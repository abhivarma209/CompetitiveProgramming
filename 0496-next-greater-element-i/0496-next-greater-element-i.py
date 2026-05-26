class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge={num:-1 for num in nums2}
        st=[]
        for i,num in enumerate(nums2):
            while len(st)>0 and nums2[st[-1]]<num:
                idx = st.pop()
                nge[nums2[idx]]=num
            st.append(i)
        res=[]
        for num in nums1:
            res.append(nge[num])
        return res