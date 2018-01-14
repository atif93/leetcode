class Solution {
    public int maxArea(int[] height) {
        int maxm = 0, i = 0, j = height.length - 1;
        
        while(i < j) {
            if(Math.min(height[i], height[j]) * (j - i) > maxm) {
                maxm = Math.min(height[i], height[j]) * (j - i);
            }  
            if(height[i] <= height[j]) {
                i++;
            } else {
                j--;
            }
        }
        return maxm;
    }
}