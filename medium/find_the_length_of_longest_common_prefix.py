from typing import List

class Trie:
    def __init__(self) -> None:
        self.root = {}
        
    def insert(self, element:int):
        element = str(element)
        cur = self.root
        for c in element:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
    def get_matching_prefix_length(self, num:int) -> int:
        count = 0
        num = str(num)
        cur = self.root
        for c in num:
            if c in cur:
                count += 1
                cur = cur[c]
            else:
                break
        return count        
        
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        ans = 0
        for num in arr1:
            trie.insert(num)
        for num in arr2:
            ans = max(ans, trie.get_matching_prefix_length(num))
        return ans
    
sol = Solution()
arr1 = [1,10,100]
arr2 = [1000]

arr1 = [1,2,3]
arr2 = [4,4,4]

arr1 = [1,232,3, 657, 77]
arr2 = [4,2,4, 65, 77]

print(sol.longestCommonPrefix(arr1, arr2))