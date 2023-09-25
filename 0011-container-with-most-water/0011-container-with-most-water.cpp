class Solution {
public:
    int maxArea(vector<int>&h) {
        int n=h.size();
        int s=0,e=n-1;
        int res=0;
        while(s<e){
            int ht=min(h[s],h[e]);
            int ba=(e-s);
            int temp=ht*ba;
            res=max(temp,res);
            if(h[s]<h[e]) s++;
            else if(h[e]<h[s]) e--;
            else{
                s++;
                e--;
            }
        }
        return res;
    }
};