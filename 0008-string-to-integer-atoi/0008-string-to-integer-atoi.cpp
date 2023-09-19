class Solution {
public:
    int myAtoi(string s) {
        int sign=1;
        int i=0;
        while(s[i]==' ')i++;
        if(s[i]=='-'){sign=-1;i++;}
        else if(s[i]=='+'){sign=1,i++;}
        int num=0;
        while(s[i]-'0'>=0 && s[i]-'0'<=9){
            if(num>INT_MAX/10 || (num==INT_MAX/10 && s[i]-'0'>7)){
                if(sign==1) return INT_MAX;
                else return INT_MIN;
            }
            num=(10*num)+(s[i]-'0');
            i++;
        }
        return num*sign;
    }
};