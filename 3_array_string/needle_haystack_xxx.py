#   Implement strStr()
class Solution:
    def is_same(self, s1: str, s2: str):
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True
            
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)-len(needle)+1):
            if self.is_same(needle, haystack[i: i+len(needle)]):
                return i
        return -1
    
s = Solution()
# haystack = "leetcode"
# needle = "leeto"
haystack = "tsadbutsad"
needle = "sad"
print(s.strStr(haystack, needle))