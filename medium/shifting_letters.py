from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # 3,5,9,4,2
        # 35942, 5942, 942, 42, 2
        suffix = [0]
        for ele in shifts[::-1]:
            suffix.append(suffix[-1]+ele)
        real = []
        for i in range(len(suffix)-1, 0, -1):
            real.append(suffix[i]%26)
        ans = ''
        for i in range(len(s)):
            ans += chr(((ord(s[i])+real[i]-ord('a'))%26)+ord('a'))
        return ans

sol = Solution()

s = "abc"
shifts = [3,5,9]

s = "aaa"
shifts = [1,2,3]

s = "aaa"
shifts = [10,20,30]

print(sol.shiftingLetters(s, shifts))            
        