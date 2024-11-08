class Solution:
    def minChanges(self, s: str) -> int:
        i = 0
        count = 0
        while i < len(s):
            if s[i] != s[i+1]:
                count += 1
            i += 2
        return count
                
sol = Solution()
s = '1001'
s = '10'
s = '0000'
s = '0100101100'
print(sol.minChanges(s))