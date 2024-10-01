from collections import defaultdict
from typing import List
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = s1.split(' ')
        l2 = s2.split(' ')
        word_count = defaultdict(int)
        for w in l1:
            word_count[w] += 1
        for w in l2:
            word_count[w] += 1
        res = []
        for k,v in word_count.items():
            if v == 1:
                res.append(k)
        print("RES: ", res)
        return res

s = Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"
s.uncommonFromSentences(s1, s2)