class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        //return lower_bound(begin(nums),end(nums),target)-begin(nums);
        int n=nums.size();
        int start=0,end=n-1;
        while(start<=end){
            int mid=(end+start)/2;
            if(nums[mid]<target) start=mid+1;
            else end=mid-1;
        }
        return start;
    }
};