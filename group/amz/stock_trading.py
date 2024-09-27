"""
You are analyzing the market trends of Amazon stocks. An AWS financial service model returned an array of integers, PnL (Profit and Loss), for your portfolio representing that in the ith month, you will either gain or lose PnL[i]. 
All reported PnL values are positive, representing gains.

As part of the analysis, you will perform the following operation on the PnL array any number of times:
- Choose any month i (0 ≤ i < n) and multiply PnL[i] by -1.

Find the maximum number of months you can afford to face a loss, i.e. have a negative PnL, such that the cumulative PnL for each of the n months remains strictly positive, i.e. remains greater than 0.
Note: The cumulative PnL for the ith month is defined as the sum of PnL from the starting month up to the ith month. For example, the cumulative PnL for the PnL = [3, -2, 5, -6, 1] is [3, 1, 6, 0, 1].
"""

import heapq
class Solution:
    def max_months_can_afford(self, PnL: list):
        negative_month = []
        cumulative = 0
        for i in range(len(PnL)):
            val = PnL[i]
            if cumulative - val >= 1:
                heapq.heappush(negative_month, -val)
                cumulative -= val  # add -val
            else:
                if len(negative_month) > 0:
                    smallest = negative_month[0]
                    if -smallest > val:
                        heapq.heappop(negative_month)
                        heapq.heappush(negative_month, -val)
                        cumulative = cumulative + 2*(-smallest) - val  # replace -val with new -val_
                    else:
                        cumulative += val  # add +val
                else:
                    cumulative += val  # add +val
        return len(negative_month)
    
sol = Solution()
PnL = [9,7,6,5,4,4,3,2]  # [-5, -4, -4, -3, -2]
# PnL = [5,7,3,  4,  6,  9,   5,   2,    7,  6,  7]  # [-7, -5, -6, -2, -3, -4]
print(sol.max_months_can_afford(PnL)) 

"""
Time complexity: O(N*log N), N = len(PnL). We iterate PnL, in each loop, we do priority heap operation which costs O(log N), therefore, O(N*log N) in overall
Space complexity: O(N)
"""
