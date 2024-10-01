
class Solution:
    def rob(self, nums: list[int]) -> int:
        nums = [2, 7, 9,  3,  1,  6,   2,  2,  5,  1,  2,  1,  1,  2,]
        i = [   2, 7, 11, 10, 12, 17,  14, 19, 22, 20, 24, 23, 25, 26]
        # length < 4
        l = len(nums)
        if l == 1 or l == 2:
            return max(nums)
        if l == 3:
            return max(nums[2]+nums[0], nums[1])
        # len >=4
        dp = [-1]*len(nums)
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[2] + nums[0]
        for idx in range(3, len(nums)):
            dp[idx] = max(dp[idx-2],dp[idx-3]) + nums[idx]
        print(dp)
        print('res: ', max(dp[len(dp)-1], dp[len(dp)-2]))
        return max(dp[len(dp)-1], dp[len(dp)-2])
        
s = Solution()
s.rob(None)
        