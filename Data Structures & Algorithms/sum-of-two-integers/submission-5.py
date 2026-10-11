class Solution:
    def getSum(self, a: int, b: int) -> int:
    
        mask = 0xFFFFFFFF

        while a != 0:
            c = ((a & b) << 1) & mask
            b = (b ^ a) & mask
            a = c

        return b if b <= 0x7FFFFFFF else ~(b ^ mask)