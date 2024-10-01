class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        nums = [2,39,40,41,3,4,5,8,9]
        sub = [nums[0]]
        
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # Find the first element in sub that is greater than or equal to num
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num
        print(len(sub))
        return len(sub)
    
s = Solution()
s.lengthOfLIS(None)