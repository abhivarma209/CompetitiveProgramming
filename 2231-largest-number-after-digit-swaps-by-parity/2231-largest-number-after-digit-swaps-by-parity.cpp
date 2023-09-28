class Solution {
public:
    int largestInteger(int num) {
        string x=to_string(num);
        vector<int>v(10);
        for(char ch: x) v[ch-'0']++;
        int res=0;
        for(int i=0;i<x.size();i++){
            bool even=false;
            if((x[i]-'0')%2==0) even = true;
            int j;
            even ? j=8 : j=9;
            while(j>=0){
                if(v[j]>0){
                    res*=10;
                    res+=j;
                    v[j]--;
                    break;
                }
                j-=2;
            }
        }
        return res;
    }
};