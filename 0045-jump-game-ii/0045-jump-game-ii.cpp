class Solution {
public:
    int jump(vector<int>& nums) {
        int n=nums.size();
        int i=0;
        int res=0;
        if(n==1) return 0;
        while(i<n){
            int x=i+nums[i];
            if(x>=n-1) return res+1;
            int temp=0;
            for(int j=i+1;j<=x;j++){
                int y=temp;
                temp=max(temp,j+nums[j]);
                if(y!=temp) i=j;
            }
            res++;
        }
        return res;
    }
};