class Solution {
    public int removeElement(int[] nums, int val) {
        if(nums.length <= 0) {
            return 0;
        }
        int prev_idx = -1;
        for(int i = 0; i < nums.length; i++) {
            if(val != nums[i]) {
                nums[++prev_idx] = nums[i];
            }
        }
        return prev_idx + 1;
    }
}