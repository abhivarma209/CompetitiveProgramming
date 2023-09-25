class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int n=s.size();
        int ones=0;
        for(auto i:s){
            if(i=='1') ones++;
        }
        string res="";
        for(int i=0;i<ones-1;i++) res+='1';
        for(int i=0;i<n-ones;i++) res+='0';
        res+='1';
        return res;
    }
};