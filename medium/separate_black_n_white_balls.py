class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        s = list(s)
        i = len(s) - 1
        # 01100110110010111
        while i>=0 and s[i] != '0':
            i -= 1
        # i : first 0
        j = i-1
        while j >= 0 and s[j] != '1' :
            j -= 1
        # j : first 1 after i
        if j >= 0:
            s[j] = '0'
            s[i] = '1'
            count += i - j
            i = i - 1
            j = j - 1
        else:
            return count
        
        while True:
            while i>= 0 and s[i] != '0':
                i -= 1
            # i : first 0
            while j >= 0 and s[j] != '1' :
                j -= 1
            # j : first 1 after i
            
            # move 1 at j-th to i-th
            if j >= 0:
                s[j] = '0'
                s[i] = '1'
                count += i - j
                i = i - 1
                j = j - 1
            else:
                break
                
        return count
    
sol = Solution()     
# s = "101"  
# s = "100" # 2
# s = "0111" # 0
# s = "01100110110010111"  # 27
#             00111111 , 
print(sol.minimumSteps(s))
        
