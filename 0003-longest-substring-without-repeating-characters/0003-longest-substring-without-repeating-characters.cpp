class Solution {
public:
    int lengthOfLongestSubstring(string s) {
       set<char> se;
        int n=s.size();
        int i=0,j=0;
        int ans=0;
        while(i<n && j<n){
            if(se.count(s[i])==0){
                se.insert(s[i]);
                i++;
                ans= max(ans,(int)se.size());
            }
            else{
                se.erase(s[j]);
                j++;
            }
        }
        return ans;
    }
};