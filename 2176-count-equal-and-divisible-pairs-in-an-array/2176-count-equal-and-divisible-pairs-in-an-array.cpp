class Solution {
public:
    int countPairs(vector<int>& nums, int k) {
        int sz=nums.size();
        int res=0;
        for(int i=0;i<sz;i++){
            for(int j=i+1;j<sz;j++){
                if((i*j)%k != 0) continue;
                if(nums[j]==nums[i]) res++;;
            }
        }
        return res;
    }
};