class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        //handling empty input
        if(intervals.empty()){
            return {newInterval};
        }
        //preparing for Binary Search
        int n = intervals.size();
        //Remember new Interval format is a vector with 2 values, where the first value is a start time and the 2nd value is end time.
        //its not a map so dont read it as one. It won't have any .first/.second calls;
        int target = newInterval[0];//target= start time of new Interval
        int l = 0, r = n-1;
        //this finds the first interval whose start >= newInterval.start
        while(l<=r){
            int mid = (l+r)/2;
            if(intervals[mid][0] < target){
                l = mid + 1;
            } else{
                r = mid - 1;
            }
        }
        intervals.insert(intervals.begin() + l, newInterval);
        //it 1 : l=1, intervals.begin()[index to pointer 0]+left = [1,3]+1 = [6,9], so it inserts newInterval int the vector at index left
        //intervals = [[1,3]. [2,5], [6,9]] 

        //Merging intervals
        vector<vector<int>> res;
        for(auto& interval:intervals){
            //Case1: no overlap -> push interval
            if(res.empty()||res.back()[1]<interval[0]){
                res.push_back(interval);
            }else{
                //res.back()[1] represents the end value of the last interval vector in the result vector
                                            //back()
                //res = [{start1,end1} , {start2, end2}]
                //                          0       1
                res.back()[1] = max(res.back()[1], interval[1]);
                //this means the intervals overlap
            }
        }
        return res;
    }
};
