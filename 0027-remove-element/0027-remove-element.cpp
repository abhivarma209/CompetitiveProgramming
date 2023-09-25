class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n=nums.size();
        int x=0,y=0;
        while(x<n && y<n){
            if(nums[x]==val) break;
            x++;y++;
        }
        while(x<n && y<n){
            while(x<n){
                if(nums[x]==val) break;
                else x++;
            }
            while(y<n){
                if(nums[y]!=val) break;
                else y++;
            }
            if(x<n && y<n)swap(nums[x],nums[y]);
        }
        int res=0;
        for(auto x:nums){
            if(x==val) break;
            res++;
        }
        return res;
    }
};