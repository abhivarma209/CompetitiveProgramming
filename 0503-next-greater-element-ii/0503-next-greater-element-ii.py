class Solution:
    def nge(self,arr: List[int]):
        st,res=[],[-1]*(len(arr))
        for i,num in enumerate(arr):
            while len(st)>0 and arr[st[-1]]<num:
                idx=st.pop()
                res[idx]=num
            st.append(i)
        return res
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        inp=nums.copy()
        sub_arr=nums[:-1]
        inp.extend(sub_arr)
        res=self.nge(inp)
        return res[0:len(nums)]