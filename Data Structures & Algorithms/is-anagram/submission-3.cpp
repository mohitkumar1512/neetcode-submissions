class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> mp;
        unordered_map<char, int> mp2;

        for (auto c : s){
            if(mp.count(c)){
                mp[c] += 1;
                
            }
            else{
                mp[c] = 1;
            }
        }
        for (auto c : t){
            if(mp2.count(c)){
                mp2[c] += 1;
                
            }
            else{
                mp2[c] = 1;
            }
        }
        return mp == mp2;
    }
};
