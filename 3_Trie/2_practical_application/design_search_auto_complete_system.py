from typing import List


# class AutocompleteSystem:
    
#     def insert(self, word, times):
#         cur = self.root
#         for i, c in enumerate(word):
#             if c in cur:
#                 top3 = cur[c]['top3hot'] 
#                 min_freq, sen, id = 1000, "", 0
#                 print(f"---cur[{c}]['top3hot'] : {top3}")
#                 print(f"-> len of top 3: {len(top3)}")
#                 if len(top3) < 3:
                    
#                     cur[c]['top3hot'].append([times, word])
#                     print(f"cur[{c}]['top3hot']: {cur[c]['top3hot']}")
#                     cur = cur[c]
#                     continue
#                 else:
#                     words = [ word for _, word in top3]
                    
#                     for i1 in range(len(words)):
#                         if word == words[i1]:
#                             _times = top3[i1][0]
#                             cur[c]['top3hot'][i1] = [_times + 1, word]
#                     else:
#                         for idx, pair in enumerate(top3):
#                             freq, sentence = pair
#                             if freq < min_freq:
#                                 min_freq = freq
#                                 sen = sentence
#                                 id = idx
#                         if times > min_freq or ( times == min_freq and word < sen ):
#                             del top3[id]
#                             cur[c]['top3hot'].append([times, word])                        
                        
#             else:
#                 cur[c] = {'top3hot': [ [times, word] ]}    
#             if i == len(word) - 1:
#                 if c in cur and 'count' in cur[c]:
#                     cur[c]['count'] += 1
#                 else:
#                     cur[c]['count'] = times
#             print(f"cur[{c}]: {cur[c]}")
#             cur = cur[c]
            
#     def __init__(self, sentences: List[str], times: List[int]):
#         self.root = {}
#         for i in range(len(sentences)):
#             self.insert(sentences[i], times[i])
            
#         self.cur = self.root
#         self.last_word = ""
#         self.count = 0
#         self.last_c = None

#     def input(self, c: str) -> List[str]:
#         if c == '#' :
#             self.last_word = ""
#             self.cur = self.root
#             self.insert(self.last_word, 1)
            
#             return []
        
#         self.last_word = self.last_word + c
#         # print(f"last word: <>{self.last_word}<>")
#         top3 = None
#         if c in self.cur:
#             top3 = []
#             for _, sentence in self.cur[c]['top3hot']:
#                 top3.append(sentence)
#         else:
#             self.cur[c] = {'top3hot': [ [1, self.last_word] ]}    
#         self.cur = self.cur[c]
#         self.last_c = c
            
#         return top3


import heapq

class AutocompleteSystem:
    base = 29
    lim = 2^61 - 1
    last_word = ""
    last_hash = 0
    
    def get_hash(self, cur_hash: int, next_c:str) -> int:
        return (cur_hash*self.base + ord(next_c) - 96) % self.lim
    
    def __init__(self, sentences: List[str], times: List[int]):
        
        self.prefix_hashes = dict()
        self.updated_sentences = dict()
        for i, sen in enumerate(sentences):
            if sen not in self.updated_sentences:
                self.updated_sentences[sen] = times[i]
            else:
                self.updated_sentences[sen] += times[i]
        
        
        for sentence, time in self.updated_sentences.items():
            cur_hash = 0
            for c in sentence:
                cur_hash = self.get_hash(cur_hash, c)
                if cur_hash in self.prefix_hashes:
                    hq = self.prefix_hashes[cur_hash] 
                    if len(hq) < 3:
                        heapq.heappush(self.prefix_hashes[cur_hash], [-time, sentence])
                    else:
                        smallest = hq[2]
                        freq, sen = smallest[0], smallest[1]
                        freq = -freq
                        if time > freq or (time == freq and sen > sentence):
                            heapq.heappop(self.prefix_hashes[cur_hash])
                            heapq.heappush(self.prefix_hashes[cur_hash], [-time, sentence])
                            
                else:
                    self.prefix_hashes[cur_hash] = [[-times[i], sentence]]
                
    def input(self, c: str) -> List[str]:
        if c == "#":
            # insert last word
            if self.last_word in self.updated_sentences:
                self.updated_sentences[self.last_word] += 1
            else:
                self.updated_sentences[self.last_word] = 1
                
            
            # init again
            self.last_word = ""
            
            return []
            
        self.last_word += c
        self.last_hash = self.get_hash(self.last_hash, c)
        top3 = self.prefix_hashes[self.last_hash]
        ans = []
        
nlkjnjnb          

# Your AutocompleteSystem object will be instantiated and called as such:
sentences = ["i love you", "island", "iroman", "i love leetcode"]
times =      [5,           3,         2,        2]
obj = AutocompleteSystem(sentences, times)
print("---RESULT---\n------\n")
print(obj.input('i'))
print(obj.input(" "))
print(obj.input('a'))
print(obj.input('#'))

print(obj.input('#'))
print(obj.input('i'))
print(obj.input(" "))
print(obj.input('a'))
print(obj.input('#'))
print("--")

print(obj.input('i'))
print(obj.input(" "))
print(obj.input('a'))
print(obj.input('#'))
print("--")
print(obj.input('i'))
