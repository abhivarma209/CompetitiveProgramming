class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int i=0,j=0;
        int n=nums.size();
        while((i<n && nums[i]%2!=0) || (j<n && nums[j]%2!=1)){
            if(nums[i]%2==1) i++;
            if(nums[j]%2==0) j++;
        }
        if(i>=n || j>=n) return nums;
        while(i<n && j<n){
            if(i>j) swap(nums[i],nums[j]);
            if(i<j) i=j;
            if(nums[i]%2==1) i++;
            if(nums[j]%2==0) j++;
        }
        return nums;
    }
};