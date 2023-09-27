class Solution {
public:
    string decodeAtIndex(string s, int k) {
        int n=s.size();
        string res="";
        long len=0;
        for(auto ch:s){
            if(ch>='a' && ch<='z') len++;
            else len*= (ch-'0');
        }
        for(int i=n-1;i>=0;i--){
            if((len==k || k==0 ) && (s[i]>='a' && s[i]<='z')){
                res+=s[i];
                return res;
            }
            else{
                if(s[i]>='a' && s[i]<='z'){
                    len--;
                }
                else{
                    len/=(s[i]-'0');
                    k%=len;
                }
            }
        }
        return "";
    }
};