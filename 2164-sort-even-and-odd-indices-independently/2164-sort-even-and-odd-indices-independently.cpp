class Solution {
public:
    vector<int> sortEvenOdd(vector<int>& nums) {
        int n=nums.size();
        for(int i=0,j=1;i<n && j<n;){
            for(int e=i+2;e<n;e+=2){
                if(nums[e]<nums[i]) swap(nums[e],nums[i]);
            }
            for(int o=j+2;o<n;o+=2){
                if(nums[o]>nums[j]) swap(nums[o],nums[j]);
            }
            i+=2;
            j+=2;
        }
        return nums;
    }
};