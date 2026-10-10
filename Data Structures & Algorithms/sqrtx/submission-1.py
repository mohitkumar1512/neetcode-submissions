class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        res = 0
        while l <= r:
            m = (l + r) // 2
            sqr = m * m
            if sqr == x:
                
                return m

            if (sqr < x and sqr > (res * res)):
                res = m

            if sqr < x:
                l = m + 1
            else:
                r = m - 1

        return res