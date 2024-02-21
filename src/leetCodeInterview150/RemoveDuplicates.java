package leetCodeInterview150;

public class RemoveDuplicates {
	public int removeDuplicates(int[] nums) {
		int index = 0;
		int n = nums.length;
		for (int i = 0; i < n; i++) {
			if (nums[index] != nums[i]) {
				index++;
				nums[index] = nums[i];
			}
		}
		return index + 1;
	}
}
