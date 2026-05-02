class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1;
        int r = *max_element(piles.begin(), piles.end());
        int res = r; //first stores the largest value then later updates based on the valid candidate value

        while(l<=r){
            int k = (l + r) / 2; 
            long long totalTime = 0;
            for (int p : piles){
                totalTime += ceil(static_cast<double>(p)/k);   
            }
            if (totalTime <= h){
                res = k; //records this as valid candidate as its below the time limit
                r = k - 1;//but tries again slower
            } else { 
                l = k + 1;
            }
        }
        return res;
    }
};
