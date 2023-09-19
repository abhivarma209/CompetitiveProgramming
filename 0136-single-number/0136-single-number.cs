public class Solution {
    public int SingleNumber(int[] nums) {
        Array.Sort(nums);
        int n= nums.Length;
        for(int i=0;i<n;i+=2){
            if(i+1==n) return nums[i];
            if(nums[i]==nums[i+1]) continue;
            else return nums[i];
        }
        return nums[n-1];
    }
}