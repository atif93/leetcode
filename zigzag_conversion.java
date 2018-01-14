class Solution {
    public String convert(String s, int numRows) {
        StringBuilder sb = new StringBuilder();
        if(numRows == 1) {
            return s;
        }
        for(int i = 0; i < numRows; i++) {
            int next = i;
            while(next < s.length()) {
                sb.append(s.charAt(next));
                if(i == 0 || i == numRows - 1) {
                    next += 2 * numRows - 2;
                    continue;
                }
                if(next + 2 * numRows - 2 * i - 2 < s.length()) {
                    sb.append(s.charAt(next + 2 * numRows - 2 * i - 2));
                }
                next += 2 * numRows - 2;
            }
        }
        return sb.toString();
    }
}