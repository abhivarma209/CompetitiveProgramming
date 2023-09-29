class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        int n=nums.size();
        if(n==1 || n==2) return true;
        bool inc=false;
        int i=1;
        while(i<n){
            if(nums[i]>nums[i-1]){
                inc=true;
                break;
            }
            else if(nums[i]<nums[i-1]){
                inc=false;
                break;
            }
            i++;
        }
        while(i<n){
            if(inc && nums[i]<nums[i-1]) return false;
            if(!inc && nums[i]>nums[i-1]) return false;
            i++;
        }
        return true;
    }
};