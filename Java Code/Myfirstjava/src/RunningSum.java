class Solution {
    public int[] runningSum(int[] nums) {
        int temp=0;
        // int n = nums.length;
        for(int i=0;i<nums.length;i++){
            temp = temp+nums[i];
            nums[i]=temp;
        }
        return(nums);
    }
}