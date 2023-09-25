class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n=nums.size();
        int start=0,end=n-1;
        int mid;
        vector<int>res(2,-1);
        while(start<=end){
            mid=(start+end)/2;
            if(nums[mid]>target){
                end=mid-1;
            }
            else if(nums[mid]<target){
                start=mid+1;
            }
            else{
                if(mid==start || nums[mid]!=nums[mid-1]){
                    res[0]=mid;
                    break;
                }
                else{
                    end=mid-1;
                    res[0]=mid-1;
                }
            }
        }
        start=0,end=n-1;
        while(start<=end){
            mid=(start+end)/2;
            if(nums[mid]>target){
                end=mid-1;
            }
            else if(nums[mid]<target){
                start=mid+1;
            }
            else{
                if(mid==end || nums[mid]!=nums[mid+1]){
                    res[1]=mid;
                    break;
                }
                else{
                    start=mid+1;
                    res[1]=mid+1;
                }
            }
        }
        return res;
    }
};