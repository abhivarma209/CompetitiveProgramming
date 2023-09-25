class Solution {
public:
    int strStr(string h, string n) {
        int p=h.size(),q=n.size();
        for(int i=0;i<p;i++){
            if(i+q>p) break;
            if(h.substr(i,q)==n) return i;
        }
        return -1;
    }
};