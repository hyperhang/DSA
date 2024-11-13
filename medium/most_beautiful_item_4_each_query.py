from typing import List
from sortedcontainers import SortedDict

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        sd = SortedDict()
        for price, beautty in items:
            if price in sd:
                if beautty > sd[price]:
                    sd[price] = beautty
            else:
                sd[price] = beautty
        pd = SortedDict()
        for price, beautty in pd:
            
        print("new dict: \n", sd)
        ans = []
        for num in queries:
            idx = sd.bisect_left(num)
            # item_temp = sd.peekitem(idx)
            print(f"\nnum: {num}, idx: {idx}, ")
            
            if idx == len(sd):
                _item = sd.peekitem(idx-1)
                ans.append(_item[1]) # add price
            else:
                if idx == 0 and sd.peekitem(0)[0] > num:
                        ans.append(0)
                else:
                    _item = sd.peekitem(idx)
                    if _item[0] != num:
                        _item = sd.peekitem(idx-1)
                        print(f"idx: {idx-1}, item: {_item}")
                    ans.append(_item[1])
        
        return ans
        
# import bisect
# bisect.bisect_left()        
        
sol = Solution()

items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]

# items = [[1,2],[1,2],[1,3],[1,4]]
# queries = [1]

# items = [[10,1000]]
# queries = [5,6,7,10,11]

items = [[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]]

queries = [885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584]

print(sol.maximumBeauty(items, queries)   )     
        