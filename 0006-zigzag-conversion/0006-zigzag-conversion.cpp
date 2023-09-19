class Solution {
public:
    string convert(string s, int numRows) {
        int n=s.length();
        vector<string>v(numRows,"");
        for(int i=0;i<n;){
            for(int j=0;j<numRows && i<n;j++){
                v[j]+=s[i];i++;
            }
            for(int j=numRows-2;j>0 && i<n;j--){
                v[j]+=s[i];i++;
            }
        }
        string res="";
        for(int i=0;i<numRows;i++){
            res+=v[i];
        }
        return res;
    }
};