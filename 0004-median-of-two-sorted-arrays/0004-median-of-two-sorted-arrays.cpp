class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m=nums1.size(),n=nums2.size();
        int mid=(m+n)/2;
        int i=0,j=0,ind=0;
        double pres=0,prev=0;
        while(i<m || j<n){
            prev=pres;
            if(j>=n) pres=nums1[i++];
            else if(i>=m) pres=nums2[j++];
            else if(nums1[i]<nums2[j]) pres=nums1[i++];
            else pres=nums2[j++];
            ind++;
            if(ind>mid) break;
        }
        return (m+n)%2==1 ? pres:(pres+prev)/2;
    }
};