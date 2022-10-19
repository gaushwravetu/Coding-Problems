import java.util.stream.*;
class Solution {
    public int pivotIndex(int[] nums) {
        int temp=0,n = nums.length;
        int mysum = Arrays.stream(nums).sum();
        int leftsum[] = new int[n+1], rightsum[] = new int[n+1];

        for(int i=0;i<n;i++){
            leftsum[i]=temp;
            temp+=nums[i];
            rightsum[i]=mysum-temp;
        }
        for(int i=0;i<n;i++){
            if(leftsum[i]==rightsum[i]){
                return(i);
            }
        }
        return(-1);
    }
}