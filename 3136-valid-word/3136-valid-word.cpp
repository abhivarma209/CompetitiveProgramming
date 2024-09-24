class Solution {
public:
    bool isValid(string word) {
        int len=word.size();
        if(len<3) return false;
        vector<int>v(4,0);
        for(int i=0;i<len;i++){
            if(word[i]>='0' && word[i]<='9') v[0]++;
            else if(word[i]>='a' && word[i]<='z'){
                if(word[i]=='a'||word[i]=='e'||word[i]=='i'||word[i]=='o'||word[i]=='u') v[1]++;
                else v[2]++;
            }
            else if(word[i]>='A' && word[i]<='Z'){
                if(word[i]=='A'||word[i]=='E'||word[i]=='I'||word[i]=='O'||word[i]=='U') v[1]++;
                else v[2]++;
            }
            else v[3]++;
        }
        if(v[3]>0 || v[1]==0 || v[2]==0) return false;
        return true;
    }
};