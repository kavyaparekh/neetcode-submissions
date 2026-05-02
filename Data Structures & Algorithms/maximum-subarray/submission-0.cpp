class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = nums[0];//best sum seen so far;
        int currSum = nums[0];
        for(int i = 1; i < nums.size(); i++){
            int x = nums[i];
            currSum = max(x, x + currSum);
            maxSum = max(maxSum, currSum);
        }
        return maxSum;
    }
};
