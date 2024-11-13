from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        forward = [0]*len(prices)
        backward = [0]*len(prices)
        cur_best_profit = 0
        cur_min = 1e6
        for i, price in enumerate(prices):
            if price < cur_min:
                cur_min = price
            elif price - cur_min > cur_best_profit:
                cur_best_profit = price - cur_min
            forward[i] = cur_best_profit
        print(forward)
        
        cur_best_profit = 0
        cur_min = 1e6
        cur_max = 0
        for i, price in enumerate(prices[::-1]):
            if price < cur_min:
                cur_min = price
            if price > cur_max:
                cur_max = price
            cur_best_profit = max(cur_best_profit, cur_max - price)
            backward[len(prices)-1-i] = cur_best_profit
        print(backward)  
        
        max_profit = max(max(forward), max(backward))
        for i in range(1, len(prices)):
            temp = forward[i-1] + backward[i]
            max_profit = max(max_profit, temp)
        return max_profit
            
            

sol = Solution()
prices = [1,2,3,4,5]
# prices = [3,3,5,0,0,3,1,4]
prices = [7,6,4,3,1]
print(sol.maxProfit(prices)   )
            
        