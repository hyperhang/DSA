from collections import defaultdict
import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def check(d1: defaultdict, d2: defaultdict):
            for i in range(26):
                if d1[chr(i+ord('a'))] != d2[chr(i+ord('a'))]:
                    print(f"{chr(i+ord('a'))}, {d1[chr(i+ord('a'))]} != {d2[chr(i+ord('a'))]}" )
                    return False
            return True
        if len(s1) > len(s2):
            return False
        freq = defaultdict(int)
        for c in s1:
            freq[c] = freq[c] + 1
        
        windows = len(s1)
        current = defaultdict(int)
        # for i in range(26): # init
        #     current[chr(i+ord('a'))] = 0
        for i in range(windows): # init
            current[s2[i]] += 1
        print("init:\n", current)
        if check(current, freq):
            return True
            
        for i in range(1,len(s2)-windows+1):
            current[s2[i-1]] -= 1
            current[s2[i+windows-1]] += 1
            print(f"s2[{i}:{i+windows-1}], current: {current}")
            if check(current, freq):
                return True
        return False
            
            
            
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_1 = Counter(s1)
        counter_2 = Counter()
        left = 0
        for right in range(len(s2)):
            counter_2[s2[right]] += 1
            if right - left + 1 > len(s1):
                counter_2[s2[left]] -= 1
                left += 1
            if counter_2 == counter_1:
                return True
        return False
    
sol = Solution()
s1 = "ab"
s2 = "eidbaooo"

s1 = "ab"
s2 = "eidboaoo"

# s1 = "yebbaw"
# s2 = "bwexbbeaebwbyw" # true

# s1 = 'adc'
# s2 = 'dcda'
print(sol.checkInclusion(s1, s2) )                        

