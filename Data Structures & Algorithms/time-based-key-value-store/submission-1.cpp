class TimeMap {
public:
unordered_map<string, vector<pair<int,string>>> mp;
    TimeMap() {
        
    }
    //T.C for set is O(1)
    void set(string key, string value, int timestamp) {
        mp[key].push_back({timestamp, value});
    }
    //SC is O(m*n) n=num of vals associated with a key
    //m is total number of keys.
    string get(string key, int timestamp) {
        //TC is O(log n)
        auto& values = mp[key];
        int l = 0, r = values.size()-1;
        string result = "";
        while(l <= r){
            int mid = (l+r)/2;
            if(values[mid].first <= timestamp){
                result = values[mid].second;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return result;
    }
};
