class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {
        vector<int>v(101,0);
        int sz=nums.size();
        int res=0;
        for(int i=0;i<sz;i++){
            v[nums[i]]++;
            if(nums[i]-k>0 && v[nums[i]-k]>0) res+=v[nums[i]-k];
            if(nums[i]+k<101 && v[nums[i]+k]>0) res+=v[nums[i]+k];
        }
        return res;
    }
};