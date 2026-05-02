class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int,int>> pair;
        for(int i = 0; i < n; i++){
            pair.push_back({position[i], speed[i]});
        }
        sort(pair.rbegin(), pair.rend());
        vector<double> stack;
        for(auto& p : pair){
            stack.push_back((double)(target - p.first) / p.second);
            //stack.back() : gives most recent car's time to target.(the behind car)
            //stack.size() - 2 : the car ahead / the fleet ahead
            if(stack.size() >= 2 && stack.back() <= stack[stack.size() - 2]){
                stack.pop_back(); //pops the recent car because it catches up to the fleet ahead 
            }
        }
        return stack.size();
    }
};