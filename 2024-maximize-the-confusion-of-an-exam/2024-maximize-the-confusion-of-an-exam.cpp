class Solution {
public:
    int helper(string a,char c,int k){
        int n=a.size();
        int i=0,j=0,res=0,count=0;
        while(j<n){
            if(a[j]==c) count++;
            while(i<n && count>k){
                if(a[i]==c) count--;
                i++;
            }
            res=max(res,j-i+1);
            j++;
        }
        return res;
    }
    int maxConsecutiveAnswers(string answerKey, int k) {
        return max(helper(answerKey,'T',k),helper(answerKey,'F',k));
    }
};