class Solution {
public:

    string encode(vector<string>& strs) {
        string encodedString;
        for(auto& s:strs){
            encodedString += s;
            encodedString += '\x1E';
        }
        cout<<encodedString;
        return encodedString;
        
    }

    vector<string> decode(string s) {
        vector<string> decodedStrings;
        string current;
        for(int i=0;i<s.length();i++){
            if(s[i]=='\x1E'){
                decodedStrings.push_back(current);
                current.clear();
            } else{
                current += s[i];
                
            }
        }
        return decodedStrings;
    }
};
