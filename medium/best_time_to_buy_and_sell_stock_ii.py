from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = 1e5
        total = 0
        for price in prices:
            if cur_min > price:
                cur_min = price
            else:
                total += price - cur_min
                cur_min = price
            print(f"curmin: {cur_min} - total: {total}")
            
        return total
    
prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
sol = Solution()
print(sol.maxProfit(prices))
                
       