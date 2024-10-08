from typing import List
from collections import defaultdict

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        added = sum(skill)/(len(skill)//2)
        if added != int(added):
            return -1
        added = int(added)
        freq = defaultdict(int)
        for ele in skill:
            freq[ele] += 1
        chem = 0 
        for ele in skill:
            if freq[ele] != 0:
                if freq[added-ele] == 0:
                    return -1
                else:
                    freq[ele] -= 1
                    freq[added-ele] -= 1
                    chem += ele*(added-ele)
        return chem

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        sumpair = sum(skill)/(len(skill)//2)
        if sumpair != int(sumpair):
            return -1
        sumpair = int(sumpair)
        i, j = 0, len(skill) - 1
        ans = 0
        while i < j:
            if skill[i] + skill[j] != sumpair :
                return -1
            ans += skill[i]*skill[j]
            i += 1
            j -= 1
        return ans
        

sol = Solution()
skill = [3,2,5,1,3,4]
# skill = [1,4,4,1]
print(sol.dividePlayers(skill))