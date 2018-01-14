class Solution {
    public int myAtoi(String str) {
        if(str.length() == 0) {
            return 0;
        }
        int i = 0, sgn = 1, res = 0;
        while(str.charAt(i) == ' ') {
            i++;
            if(i >= str.length()) {
                return res;
            }
        }
        if(str.charAt(i) == '+') {
            i++;
        } else if (str.charAt(i) == '-') {
            sgn = -1;
            i++;
        }
        if(i >= str.length()) {
            return res;
        }
        long res2 = 0;
        while(str.charAt(i) >= 48 && str.charAt(i) <= 57) {
            res2 = res2 * 10 + (str.charAt(i) - 48);
            if(res2 * sgn < Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            } else if (res2 * sgn > Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            }
            i++;
            if(i >= str.length()) {
                return (int)res2 * sgn;
            }
        }
        return (int)res2 * sgn;
    }
}