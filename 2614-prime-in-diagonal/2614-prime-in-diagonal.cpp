class Solution {
public:
    bool isPrime (int num){
        int x=sqrt(num);
        if(num==1) return 0;
        for(int i=2;i<=x;i++){
            if(num%i==0) return 0;
        }
        return 1;
    }
    int diagonalPrime(vector<vector<int>>& nums) {
        int res=0;
        int sz=nums[0].size();
        for(int i=0;i<sz;i++){
            if(isPrime(nums[i][i])) res=max(res,nums[i][i]);
            if(isPrime(nums[i][sz-1-i])) res=max(res,nums[i][sz-1-i]);
        }
        return res;
    }
};