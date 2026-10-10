class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;  
        int s1Count[26] = {0}; 
        int s2Count[26] = {0}; 
        for (int i = 0; i < s1.size(); i++){
            s1Count[s1[i] - 'a'] += 1;
            s2Count[s2[i] - 'a'] += 1;
        }

        int matches = 0;
        for (int i = 0; i < 26; i++) {
            if (s1Count[i] == s2Count[i]) matches++;
        }

        int l = 0;
        for (int i = s1.size(); i < s2.size(); i++){
            if (matches == 26) return true;

            int index = s2[i] - 'a';
            s2Count[index] += 1;
            if (s1Count[index] == s2Count[index]) matches += 1;
            else if (s1Count[index] + 1 == s2Count[index]) matches -= 1;

            int left = s2[i - s1.size()] - 'a';
            s2Count[left]--;
            if (s2Count[left] == s1Count[left])      matches++;
            else if (s2Count[left] + 1 == s1Count[left]) matches--;
        }
        return matches == 26;
    }
};
