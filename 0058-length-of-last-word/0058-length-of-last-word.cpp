class Solution {
public:
    int lengthOfLastWord(string s) {
        reverse(s.begin(),s.end());
        transform(s.begin(),s.end(),s.begin(),::tolower);
        int n=s.size();
        int i=0;
        for(i=0;i<n;i++){
            if(s[i]>='a' && s[i]<='z') break;
        }
        int res=0;
        for(;i<n;i++){
            if(s[i]>='a' && s[i]<='z'){
                res++;
            }
            else break;
        }
        return res;
    }
};