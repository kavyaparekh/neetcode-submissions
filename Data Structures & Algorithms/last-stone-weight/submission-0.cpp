class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxHeap;
        for(int stone : stones){
            maxHeap.push(stone);
        }

        while(maxHeap.size()>1){
            int left = maxHeap.top();
            maxHeap.pop();
            int right = maxHeap.top();
            maxHeap.pop();
            if(right<left){
                maxHeap.push(left - right);
            }
        }
        maxHeap.push(0);
        return maxHeap.top();
    }
};
