class Solution {
public:
    int lengthOfLongestSubstring(string s) {
            unordered_set<char> seen;
    int maxy = 0;
    int l = 0;

    for (int r = 0; r < s.size(); r++) {
        // shrink window from left until duplicate is removed
        while (seen.count(s[r])) {
            seen.erase(s[l]);
            l++;
        }
        seen.insert(s[r]);
        maxy = max(maxy, r - l + 1);
    }

    return maxy;

    }
};
