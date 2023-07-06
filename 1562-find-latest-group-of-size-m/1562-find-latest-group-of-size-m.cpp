class Solution {
public:
    int findLatestStep(vector<int>& arr, int m) {
       int n=arr.size();
       vector<int>v(n+1);
       int res=-2;
       int count=0;
       for(int i=0;i<n;i++){
           if(v[arr[i]-1]==0){
               v[arr[i]]=1;
           }
           bool flag=false;
           if(v[arr[i]-1]!=0){
               flag=true;
               v[arr[i]]=v[arr[i]-1]+1;
               if(v[arr[i]-1]==m) count--;
           }
           if(arr[i]+1<=n && v[arr[i]+1]!=0){
               v[arr[i]]+=v[arr[i]+1];
               if(v[arr[i]+1]==m) count--;
               v[arr[i]+v[arr[i]+1]]=v[arr[i]];
           }
           if(flag)v[arr[i]-v[arr[i]-1]]=v[arr[i]];
           if(v[arr[i]]==m){
               count++;
               res=i;
           }
           if(count>0) res=i;
       }
       return res+1;
    }
};
