class Solution:
    def prefM(self,nums):
        pref=[1]
        for i in range(len(nums)-1):
            pref.append(nums[i]*pref[-1])
        return pref
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref,suff=self.prefM(nums),self.prefM(nums[::-1])
        suff=suff[::-1]
        return [pref[i]*suff[i] for i in range(len(nums))]
        
        
