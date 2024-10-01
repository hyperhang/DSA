# class Solution:
#     max_length = 0
    # def findTheLongestSubstring(self, s: str) -> int:
    #     count = {'a': [0], 'o': [0], 'e':[0], 'u':[0], 'i':[0]}
    #     if s[0] in count:
    #         count[s[0]] = [1]
    #     for i, c in enumerate(s[1:]):
    #         for k in count.keys():
    #             count[k].append(count[k][-1])
    #         if c in count:
    #             count[c][-1] += 1 
                
    #     print(count)
        
    #     def contains_even_char(left: int, right: int, char: str):
    #         if left == 0:
    #             return count[char][right] % 2 == 0
    #         else:
    #             return count[char][right] - count[char][left-1] % 2 == 0
    #     def contains_even_vowels(left: int, right: int):
    #         flag = True
    #         for char in ['a', 'o', 'e', 'u', 'i']:
    #             if left == 0:
    #                 flag = count[char][right] % 2 == 0
    #             else:
    #                 flag = count[char][right] - count[char][left-1] % 2 == 0   
    #             if flag == False:
    #                 print("wrong at : ", char)
    #                 print("count left: ", count[char][left])
    #                 print("count right: ", count[char][right])
    #                 return False
    #         return True
        
    #     def check_range(left, right):
    #         if left < 0 or left > right:
    #             return
    #         for key in count.keys():
    #             if contains_even_char(left, right, key):
    #                 pass
    #             else:
    #                 while left < len(s) and s[left] != 'a':
    #                     left += 1
    #                 check_range(left-1, right)
    #                 check_range(left+1, right)
    #     maxi, maxj = 0,0
    #     for i in range(len(s)):
    #         for j in range(i,len(s)):
    #             print("i, j ", i, j)
    #             if contains_even_vowels(i, j):
    #                 if self.max_length < j-i+1:
    #                     self.max_length = j-i+1
    #                     maxi, maxj = i, j
    #     # check_range(0, len(s)-1)    
    #     print("MAX: ", self.max_length)
    #     print("substring:", s[maxi:maxj+1])
    #     print("count: ", count['a'][14])
    #     print("S[15:]", s[15:])
    #     print("s[15:] has even vowels? :", contains_even_vowels(15, len(s)-1))
    #     return self.max_length        
                     
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        convert = {'a': 2**0, 'e': 2**1, 'i': 2**2, 'o': 2**3, 'u': 2**4}
        prefix = [0]
        for c in s:
            if c in ['a', 'o', 'e', 'u', 'i']:
                prefix.append(prefix[-1]^convert[c])
            else:
                prefix.append(prefix[-1])
        init = {0:0}
        answer = 0
        for i in range(1, len(prefix)):
            if prefix[i] in init:
                answer = max(answer, i - init[prefix[i]])
            else:
                init[prefix[i]] = i
        return answer

     
        
sol = Solution()
s = "leetcodegreat"
print(sol.findTheLongestSubstring(s))