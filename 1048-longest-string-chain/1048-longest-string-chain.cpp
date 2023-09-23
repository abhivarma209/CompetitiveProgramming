class Solution {
public:
    bool subSequence(string a, string b){
        int m=a.size(),n=b.size();
        int i=0,j=0;
        while(i<m && j<n){
            if(a[i]==b[j]) i++;
            j++;
        }
        return i>=m?true:false;
    }
    int longestStrChain(vector<string>& words) {
        int n=words.size();
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(words[i].size()>words[j].size()) swap(words[i],words[j]);
            }
        }
        vector<int>v(n,1);
        if(n==1) return 1;
        int res=1;
        for(int i=n-2;i>=0;i--){
            for(int j=i+1;j<n;j++){
                if(subSequence(words[i],words[j]) && words[i].size()+1==words[j].size()){
                    v[i]=max(v[i],v[j]+1);
                }
            }
            cout<<v[i]<<" ";
            res=max(res,v[i]);
        }
        cout<<endl;
        return res;
    }
};