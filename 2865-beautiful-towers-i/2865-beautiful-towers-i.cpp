class Solution {
public:
    long long maximumSumOfHeights(vector<int>& maxHeights) {
        long long res=0;
        int n=maxHeights.size();
        for(int i=0;i<n;i++){
            long long temp=maxHeights[i];
            int prev=maxHeights[i];
            for(int j=i-1;j>=0;j--){
                if(maxHeights[j]>prev){
                    temp+=prev;
                }
                else{
                    temp+=maxHeights[j];
                    prev=maxHeights[j];
                }
            }
            prev=maxHeights[i];
            for(int k=i+1;k<n;k++){
                if(maxHeights[k]>prev){
                    temp+=prev;
                }
                else{
                    temp+=maxHeights[k];
                    prev=maxHeights[k];
                }
            }
            cout<<temp<<" ";
            res=max(res,temp);
        }
        cout<<endl;
        return res;
    }
};