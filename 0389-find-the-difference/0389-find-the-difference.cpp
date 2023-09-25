class Solution {
public:
    char findTheDifference(string s, string t) {
        vector<int>v(26);
        int res=0;
        for(auto i:t) v[i-'a']++;
        for(auto i:s) v[i-'a']--;
        for(int i=0;i<26;i++){
            if(v[i]==1){
                res=i;
                break;
            }
        }
        return res+'a';
    }
};