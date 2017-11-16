class Solution {
    public String longestPalindrome(String s) {
        int[][] smap = new int[s.length()][s.length()];
        int max = 0, maxl = 0, maxr = 0;
        
        for (int i = 0; i < s.length(); i++) { // the window size
            for (int j = 0; j + i < s.length(); j++) {
                if (i == 0) {
                    smap[j][j] = 1;
                    continue;
                } else if (i == 1) {
                    if (s.charAt(j) == s.charAt(j + i)) {
                        smap[j][j + i] = 1;
                        if (max < i + 1) {
                            max = i + 1;
                            maxl = j;
                            maxr = j + i;
                        }
                    }
                    continue;
                }
                if (s.charAt(j) == s.charAt(j + i)) {
                    if (smap[j + 1][j + i - 1] == 1) {
                        smap[j][j + i] = 1;
                        if (max < i + 1) {
                            max = i + 1;
                            maxl = j;
                            maxr = j + i;
                        }
                    }
                } 
            }
        }
        
        return s.substring(maxl, maxr + 1);
    }
}