class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i, smallest, maxProfit = 0;
        
        if(prices.size() > 0) {
            smallest = prices[0];
        } else {
            return 0;
        }
        
        for(vector<int>::iterator it = prices.begin()+1; it!=prices.end(); it++ ) {
            if(smallest > *it) {
                smallest = *it;
            }
            if(*it > *(it-1)) {
                if(maxProfit < *it - smallest) {
                    maxProfit = *it - smallest;
                }
            } 
            
        }
        return maxProfit;
    }
};