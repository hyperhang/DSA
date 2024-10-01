import heapq
class Solution:
    def max_months_can_afford(self, PnL: list):
        negative_month = []
        cumulative = 0
        for i in range(len(PnL)):
            val = PnL[i]
            print("\n----\ncurrent: ", PnL[:i+1])
            if cumulative - val >= 1:
                heapq.heappush(negative_month, -val)
                cumulative -= val  # add -val
            else:
                if len(negative_month) > 0:
                    smallest = negative_month[0]
                    print("-smallest = ", -smallest)
                    if -smallest > val:
                        heapq.heappop(negative_month)
                        heapq.heappush(negative_month, -val)
                        cumulative = cumulative + 2*(-smallest) - val  # replace -val with new -val_
                    else:
                        cumulative += val  # add +val
                else:
                    cumulative += val  # add +val
            print("cumulative = ", cumulative)
            print("minus arr: ", negative_month)
        print(negative_month)
        return len(negative_month)
    
sol = Solution()
# PnL = [9,7,6,5,4,4,3,2]
PnL = [5,7,3,  4,  6,  9,   5,   2,    7,  6,  7]
print(sol.max_months_can_afford(PnL)) 