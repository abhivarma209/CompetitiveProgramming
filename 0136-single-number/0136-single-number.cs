public class Solution {
    public int SingleNumber(int[] nums) {
        int res=0;
        foreach( int x in nums){
            res^=x;
        }
        return res;
    }
}