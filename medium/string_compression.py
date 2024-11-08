from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 1, 1
        count = 1
        cur = chars[0]
        while j < len(chars):
            if chars[j] == cur:
                count += 1
            else:
                if count == 1:
                    pass
                else:
                    for c in str(count):
                        chars[i] = c
                        i += 1
                    count = 1
                    
                cur = chars[j]
                chars[i] = cur
                i += 1
                    
            j += 1
        
        if count != 1:
            for c in str(count):
                chars[i] = c
                i += 1
        end = i 
        print(chars)
        print("end: ", end)
        
            
        return end
        
        
sol = Solution()
chars = ["a","a","b","b","c","c","c"]
chars = ["a"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# chars = ["a","a","a","a","a","a","a","a","a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"]
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

print(sol.compress(chars))
            