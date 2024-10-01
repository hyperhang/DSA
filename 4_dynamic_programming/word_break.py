class Solution:
    flag = False
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        s = "applepenapple"
        wordDict = ["apple","pen"]
        s = "leetcode"
        wordDict = ["leet","code"]
        s = "catsandog"
        wordDict = ["cats","dog","sand","and","cat"]
        # flag = False
        def check(s):
            
            print("-----\ns: ",s)
            for word in wordDict:
                print(f"word, s[:len(word)]: {word}, {s[:len(word)]}")
                if word == s[:len(word)]:
                    print("word = s[:len(word)]")
                    if len(word) == len(s):
                        self.flag = True
                        print("=> flag = True")
                        return
                    check(s[len(word):]) 
            return
        
        check(s)
        if self.flag:
            return True
        else:
            return False

s = Solution()
res = s.wordBreak(None, None)
print(res)