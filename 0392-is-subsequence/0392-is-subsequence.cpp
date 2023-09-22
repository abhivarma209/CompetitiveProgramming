class Solution {
public:
    bool isSubsequence(string s, string t) {
        int n=s.length();
        int m=t.length();
        int i=0,j=0;
        while(i<n && j<m){
            char temp=s[i];
            while(j<m && t[j]!=temp){
                j++;
            }
            if(j>m) return false;
            if(t[j]==temp){
                i++;j++;
            }
        }
        if(i<n) return false;
        return true;
    }
};