class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        def check(i,j):
            count = 0
            while s[i] == goal[j] and count != len(s):
                count += 1
                i = (i+1) % len(s)
                j = (j+1) % len(goal)
                
            return count == len(s)
        
        for i in range(len(s)):
            if check(i, 0):
                return True
            
        return False
                
sol = Solution()
s = "abcde"
goal = "cdeab"

# s = "abcde"
# goal = "abced"
print(sol.rotateString(s, goal))


"""
675664535675664535

664535675 664535675
356666645
"""