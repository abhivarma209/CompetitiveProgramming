public class Solution {
    public int[] SingleNumber(int[] nums) {
        int xor=0;
        int n=nums.Length;
        foreach(int x in nums){
            xor^=x;
        }
        int firstSetBit=0;
        for(int i=0;i<32;i++){
            if( ((xor>>i) & 1)==1){
                firstSetBit=i;
                break;
            }
        }
        int res1=0,res2=0;
        for(int i=0;i<n;i++){
            if(((nums[i]>>firstSetBit)&1)==1) res1^=nums[i];
            else res2^=nums[i];
        }
        int[] res=new int[2] {res1,res2};
        return res;
    }
}