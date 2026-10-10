class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        max_profit = 0
        while right < len(prices): 
            l_price = prices[left]
            r_price = prices[right]
            print(l_price)
            print(r_price)
            max_profit = max(max_profit, r_price - l_price)
            if r_price < l_price:
                left = right
            right += 1
        
        return max_profit