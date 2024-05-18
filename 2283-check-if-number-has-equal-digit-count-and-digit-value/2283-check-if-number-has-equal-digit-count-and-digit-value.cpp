class Solution {
public:
    bool digitCount(string num) {
        int sz=num.size();
        vector<int>v(sz,0);
        for(int i=0;i<sz;i++){
            int digit=num[i]-'0';
            if(digit>=sz) return 0;
            v[digit]++;
        }
        for(int i=0;i<sz;i++){
            if(v[i]!=num[i]-'0') return 0;
        }
        return 1;
    }
};