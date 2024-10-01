from typing import List

class Trie:
    def __init__(self) -> None:
        self.root = {}
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c in cur:
                cur[c]['count'] += 1
            else:
                cur[c] = {'count': 1}
            cur = cur[c]
    
    def get_sum_score_of_all_prefix(self, word:str) -> int:
        su = 0
        cur = self.root
        for c in word:
            if c in cur:
                su += cur[c]['count']
            else:
                break
            cur = cur[c]
        return su
        

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = []
        for word in words:
            ans.append(trie.get_sum_score_of_all_prefix(word))
        print("ANS: ", ans)
        return ans
# TC: sum of length of word[i], i from 0 -> end O(K*N), N: len of words, K: max length of word[i], = O(10^6)
# SC: worst case: O(K*N) , N: len of words, K: max length of word[i], = O(10^6)
    
sol = Solution()
words = ["abc","ab","bc","b"]
words = ["abcd"]

sol.sumPrefixScores(words)
