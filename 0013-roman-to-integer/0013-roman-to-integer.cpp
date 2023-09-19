class Solution {
public:
    int roman(char a){
        if(a=='I') return 1;
        else if(a=='V') return 5;
        else if(a=='X') return 10;
        else if(a=='L') return 50;
        else if(a=='C') return 100;
        else if(a=='D') return 500;
        else if(a=='M') return 1000;
        return 0;
    }
    int romanToInt(string s) {
        int n=s.size();
        int res=roman(s[0]);
        int x=roman(s[0]);
        int i=1;
        while(i<n){
            if(s[i]==s[i-1]){
                res+=roman(s[i]);
            }
            else if(roman(s[i])>roman(s[i-1])){
                res+=roman(s[i])-2*roman(s[i-1]);
            }
            else if(roman(s[i])<roman(s[i-1])){
                res+=roman(s[i]);
            }
            i++;
        }
        return res;
    }
};