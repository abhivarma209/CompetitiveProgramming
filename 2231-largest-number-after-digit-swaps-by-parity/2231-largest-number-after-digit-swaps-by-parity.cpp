class Solution {
public:
    int largestInteger(int num) {
        string x=to_string(num);
        vector<int>v(10);
        for(char ch: x) v[ch-'0']++;
        int res=0;
        for(int i=0;i<x.size();i++){
            char ch=x[i];
            bool even=false;
            if((x[i]-'0')%2==0) even = true;
            if(even){
                for(int j=8;j>=0;j-=2){
                    if(v[j]>0){
                        res*=10;
                        res+=j;
                        v[j]--;
                        break;
                    }
                }
            }
            else{
                for(int j=9;j>=1;j-=2){
                    if(v[j]>0){
                        res*=10;
                        res+=j;
                        v[j]--;
                        break;
                    }
                }
            }
        }
        return res;
    }
};