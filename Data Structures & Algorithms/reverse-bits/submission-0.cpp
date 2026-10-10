class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;

        for (int i = 0; i < 32; i++) {
            res = (res << 1) | (n & 1);  // shift res left, plug in last bit of n
            n >>= 1;                      // move to next bit of n
        }

        return res;
    }
};
