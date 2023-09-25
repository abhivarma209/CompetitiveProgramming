class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        bool flag=false;
        int n=nums.size();
        int x;
        int i;
        for(x=n-1;x>=0;x--){
            for(i=n-1;i>x;i--){
                if(nums[i]>nums[x]){
                    int temp=nums[i];
                    nums[i]=nums[x];
                    nums[x]=temp;
                    flag=true;
                    break;
                }
            }
            if(flag) break;
        }
        
        if(!flag) reverse(nums.begin(),nums.end());
        else{
            sort(nums.begin()+x+1,nums.end());
        }
    }
};