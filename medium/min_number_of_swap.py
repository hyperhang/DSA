class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        head = 0 # count of the number of [ 
        tail = 0 # count of the number of ]
        i, j = 0, len(s)-1
        while i < j :
            if s[i] == ']' and head == 0 and s[j] == '[' and tail == 0:
                count += 1
                head += 1
                tail += 1
                i += 1
                j -= 1
            else:
                if s[i] == ']' and head != 0:
                    head -= 1
                    i += 1
                if  s[i] == '[':
                    head += 1
                    i += 1
                
                if s[j] == '[' and tail != 0:
                    tail -= 1
                    j -= 1
                if  s[j] == ']':
                    tail += 1
                    j -= 1
        return count
    
sol = Solution()
# s = "][]["
# s = "]]][[["
# s = "]]]][[[["
s = '[[]]][][[]'
print(sol.minSwaps(s))

