class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        s = "applepenapple"
        wordDict = ["apple","pen"]
        # s = "leetcode"
        # wordDict = ["leet","code"]
        # s = "catsandog"
        # wordDict = ["cats","dog","sand","and","cat"]
        dp = [0] * len(s)
        for idx in range(len(s)):
            for word in wordDict:
                if word == (s[:idx+1])[-len(word):]:
                    if (s[:idx+1])[:-len(word)] == "" or dp[idx-len(word)] == 1:
                        dp[idx] = 1
                        break
        print("dp: ", dp)
        return bool(dp[len(s)-1])

s = Solution()
res = s.wordBreak(None, None)
print(res)