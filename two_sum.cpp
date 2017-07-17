class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> index; 
        vector<int> ans;
        int i;
        for(i = 0; i < nums.size(); i++) {
            if(index.find(nums[i]) != index.end()) {
                break;
            }
            index[target - nums[i]] = i;
        }
        ans.push_back(index[nums[i]]);
        ans.push_back(i);
        return ans;
    }
};