class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length <= 0) {
            return 0;
        }
        int prev = nums[0];
        int prev_idx = 0;
        for(int i = 1; i < nums.length; i++) {
            if(prev != nums[i]) {
                nums[++prev_idx] = nums[i];
                prev = nums[i];
            }
        }
        return prev_idx + 1;
    }
}