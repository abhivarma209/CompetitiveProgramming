class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        bool flag=true;
        int j=0;
        string res="";
        while(flag){
            char temp=strs[0][j];
            for(int i=0;i<strs.size();i++){
                if(j==strs[i].size() || strs[i][j]!=temp){
                    flag=false;
                    break;
                }
            }
            if(flag) res+=temp;
            j++;
        }
        return res;
    }
};