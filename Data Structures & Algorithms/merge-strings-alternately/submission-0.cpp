class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        string res;
        int i = 0;
        while (n || m){

            if (n){
                res += word1[i];
                n -= 1;
            }
            if (m){
                res += word2[i];
                m -= 1;
            }
            i += 1;
        }
        return res;
    }
};