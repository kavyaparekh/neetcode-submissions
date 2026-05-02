class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> count;
        for (int num:nums){
            count[num]++;
        }//1->3,2->2,3->1

        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> heap;
        for (auto& entry : count){
            heap.push({entry.second,entry.first});
            if(heap.size()>k){
                heap.pop();
            }//3,1 2,2
        }
        
        vector<int> res;
        for(int i =0; i<k; i++){
            res.push_back(heap.top().second);
            heap.pop();
        }
        return res;
        
    }
};
