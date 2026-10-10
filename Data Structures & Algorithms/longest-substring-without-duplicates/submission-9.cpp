class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> lastSeen; // char --> last index seen
        int maxy = 0;
        int l = 0;

        for (int r = 0; r < s.size(); r++) {
            if (lastSeen.count(s[r]) && lastSeen[s[r]] >= l) {
                l = lastSeen[s[r]] + 1; // jump left pointer directly
            }
            lastSeen[s[r]] = r;
            maxy = max(maxy, r - l + 1);
        }

        return maxy;
    }
};
