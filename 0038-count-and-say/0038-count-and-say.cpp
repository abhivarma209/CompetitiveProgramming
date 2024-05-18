class Solution {
public:
    string countAndSay(int n) {
        string x="1";
        string res="";
        for(int i=1;i<n;i++){
            int j=0; 
            while(j<x.size()){
                char temp=x[j];
                int c=0;
                while(j<x.size() && x[j]==temp){
                    j++;
                    c++;
                }
                res+=to_string(c);
                res+=temp;
            }
            x=res;
            res.erase();
        }
        return x;
    }
};