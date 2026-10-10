class Solution {
public:
    bool isValid(string s) {
        if (s.size() <= 1) return false;
        unordered_map<char, char> mp = {{'}','{'}, {']','['}, {')','('}};
        stack<char> str; 
        for (auto c : s){
            if (c == ')' || c == '}' || c == ']'){
                if (!str.empty() && mp[c] == str.top()){
                    str.pop();
                } else{
                    return false;
                }
            }
            else{
                str.push(c);
            }

        }
        if (str.empty()) return true;
        return false;
    }
};
