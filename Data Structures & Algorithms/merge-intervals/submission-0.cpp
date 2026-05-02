class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        //edge case: no intervals
        if(intervals.empty()) return {};

        //sort intervals by start time
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> res;
        for(auto& interval : intervals){
            //if result is empty or no overlap with last interval
            if(res.empty()||res.back()[1] < interval[0]){
                res.push_back(interval);
            } //overlap case -> merger by extending end
            else{
                res.back()[1] = max(res.back()[1], interval[1]);
            }
        }
        return res;
    }
};
