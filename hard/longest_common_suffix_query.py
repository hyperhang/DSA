from typing import List

# # 1st Solution 
# class Solution:
#     lim = 2**61 - 1
#     base = 29
#     def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
#         def get_hash(current_hash:str, next_char:str) -> int:
#             return int((current_hash*self.base+ ord(next_char) - 96) % self.lim)
        
#         def get_1st_smallest_length_word_index() -> int:
#             idx = 0
#             smallest = 1e5
#             for i, word in enumerate(wordsContainer):
#                 if len(word) < smallest:
#                     smallest = len(word)
#                     idx = i
#             return idx
            
#         suffix_dict = dict()
#         # For each word in wordsContainer, we  compute the rolling hash for every suffix , 
#         # and also, build a dictionary with the key is the rolling hash, and the value is a list, 
#         # containing pairs of [length_of_original_word, index_of_suffix_in_word]
#         for idx, word in enumerate(wordsContainer):
#             cur_hash = 0
#             length = len(word)
#             for c in word[::-1]:
#                 cur_hash = get_hash(cur_hash, c)
#                 if cur_hash in suffix_dict:
#                     last_length, _ = suffix_dict[cur_hash]
#                     if last_length > length:
#                         suffix_dict[cur_hash] = [length, idx]
#                 else:
#                     suffix_dict[cur_hash] = [length, idx]    
#         print("suffix dict: \n", suffix_dict)
#         ans = []
#         first_smallest_length_word_index = get_1st_smallest_length_word_index()
#         for word in wordsQuery:
#             cur_hash = 0
#             length = len(word)
#             matching = []
#             for c in word[::-1]:
#                 cur_hash = get_hash(cur_hash, c)
#                 if cur_hash in suffix_dict:
#                     matching = suffix_dict[cur_hash]
#                 else:
#                     break
#             if len(matching) == 0:
#                 ans.append(first_smallest_length_word_index)
#                 continue
            
#             print("matching: ", matching)
#             ans.append(matching[1])
            
#         print("RESULT: ", ans)
#         return ans
    
    
    
    
    
# 2nd solution
class Trie:
    def __init__(self) -> None:
        self.root = {}
        
    def insert(self, word:str, ind: int):
        cur = self.root
        length = len(word)
        
        for c in word[::-1]:
            if c in cur:
                pre_length, pre_index = cur[c]['id']
                if pre_length > length:
                    cur[c]['id'] = [length, ind]
            else:
                cur[c]= {'id':[length, ind]}
            cur = cur[c]
    
    def get_longest_common_suffix(self, word:str, val: int) -> int:
        cur = self.root
        idx = val
        for c in word[::-1]:
            if c in cur:
                _, idx = cur[c]['id']    
                cur = cur[c]
            else:
                break
        return idx  
        
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()
        smallest = 1e5
        idx = 0
        for ind, word in enumerate(wordsContainer):
            trie.insert(word, ind)
            if smallest > len(word):
                smallest = len(word)
                idx = ind
        ans = []
        for word in wordsQuery:
            ans.append(trie.get_longest_common_suffix(word, idx))
        print("ANS: ", ans)
        return ans
    
    
sol = Solution()
wordsContainer = ["abcd","bcd","xbcd"]
wordsQuery = ["cd","bcd","xyz"]

# wordsContainer = ["abcdefgh","poiuygh","ghghgh"]
# wordsQuery = ["gh","acbfgh","acbfegh"]

sol.stringIndices(wordsContainer, wordsQuery)
            

                
            
        
        