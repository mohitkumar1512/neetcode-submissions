class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
           # move res left 
           res <<= 1

           # or the last bit of n
           res |= n & 1

           # move n to the right
           n >>= 1
           
        return res