class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        pivot = strs[0]
        common = ""
        for i in range(0, len(pivot)):
            for ele in range(1,len(strs)):
                if i == len(strs[ele]):
                    return common
                else:
                    if strs[ele][i] != pivot[i]:
                        return common
            common += pivot[i]
        return common

s = Solution()
# strs = ["dog","racecar","car"]
strs = ["flowerrr","fl","fl"]
print(s.longestCommonPrefix(strs)   )                     
            