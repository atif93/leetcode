class Solution {
public:
    int reverse(int x) {
        long long rev = 0;
        bool neg_flag = false;
        if(x < 0) {
            neg_flag = true;
            x *= -1;
        }   
        while(x!=0) {
            int dig = x % 10;
            rev = rev * 10 + dig;
            x = x / 10;
        }
        if(neg_flag == true) {
            rev *= -1;
        }
            
        if(rev < -2147483648 || rev > 2147483647) {
            return 0;
        }
        return rev;
    }
};


class Solution {
public:
    int reverse(int x) {
        long long res = 0;
        while(x) {
            res = res*10 + x%10;
            x /= 10;
        }
        return (res<INT_MIN || res>INT_MAX) ? 0 : res;
    }
};


// checks overflow
class Solution {
public:
    int reverse(int x) {
        int ans = 0;
        while (x) {
            int temp = ans * 10 + x % 10;
            if (temp / 10 != ans)
                return 0;
            ans = temp;
            x /= 10;
        }
        return ans;
    }
};