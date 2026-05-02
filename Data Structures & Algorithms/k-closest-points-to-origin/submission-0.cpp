class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        //max heap
        priority_queue<pair<int,vector<int>>> maxHeap;
        for(auto& point : points){
            //squaring x(0) and y(1) coordinates of the point
            int dist = point[0]*point[0] + point[1]*point[1];
            maxHeap.push({dist, point});
            if(maxHeap.size()>k){
                maxHeap.pop();
            }
        }
        vector<vector<int>> result;
        while(!maxHeap.empty()){
            result.push_back(maxHeap.top().second);
            maxHeap.pop();
        }
        return result;
    }
};
