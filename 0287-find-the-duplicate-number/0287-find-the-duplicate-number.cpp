class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n=nums.size();
        int low=1,high=n-1;
        while(low<=high){
            int mid=(high+low)/2;
            int cnt=0;
            for(auto i:nums){
                if(i<=mid) cnt++;
            }
            if(cnt>mid){
                high=mid-1;
            }
            else low=mid+1;
        }
        return low;
    }
};