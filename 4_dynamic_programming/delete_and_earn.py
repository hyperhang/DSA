class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:

        nums = [2,2,3,3,3,4]
        # nums = [2,2,2]
        nums = [3, 4, 2]
        nums = [2,2,3,3,3,4,4,5]
        nums = [3,1]
        s = set(nums)
        nums.sort()
        print(nums)
        unique = []
        freq = []
        c, i = 0, 0
        while i < len(nums):
            if c == 0:
                unique.append(nums[i])
                c += 1
                freq.append(c)
            elif nums[i] == nums[i-1]:
                c += 1
                freq[len(freq)-1] = c
            else:
                c = 0
                i -= 1
            i += 1
        print("unique: ", unique)
        print("freq:   ", freq)

        i = 2
        dp = [0]*len(unique)
        dp[0] = unique[0]*freq[0]
        if len(unique) == 1:
            print("dp: ", dp)
            return dp[0]
        if unique[1] == unique[0] + 1:
            dp[1] = max(unique[0]*freq[0], unique[1]*freq[1])
        else:
            dp[1] = unique[0]*freq[0] + unique[1]*freq[1]
        
        while i < len(unique):
            if unique[i] == unique[i-1] + 1:
                dp[i] = max(unique[i]*freq[i] + dp[i-2], dp[i-1])  
            else:
                dp[i] = dp[i-1] + unique[i]*freq[i]
            i += 1
            
        print("dp: ", dp)
        return dp[len(dp) -1]
    
s = Solution()
s.deleteAndEarn(None)
                
