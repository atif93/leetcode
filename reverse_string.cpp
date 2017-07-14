class Solution {
public:
    string reverseString(string s) {
        int i = 0, j = s.size() - 1;
        char temp;
        while(i < j) {
            temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            i++;
            j--;
        }
        return s;
    }
};

/*****************************************/

class Solution {
public:
    string reverseString(string s) {
        int i = 0, j = s.size() - 1;
        while(i < j) {
            swap(s[i++], s[j--]); // takes elements to swap. reverse() [present in algorithm] takes positions.
        }
        return s;
    }
};