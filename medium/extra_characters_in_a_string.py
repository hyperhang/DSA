from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        max_dic_len = 0
        for w in dictionary:
            max_dic_len = max(max_dic_len, len(w))
        
        dp = [0]*len(s)
        if s[0] in dictionary:
            dp[0] = 0
        else:
            dp[0] = 1
        for i in range(1, len(s)):
            print(f"\n---------\ns[:{i+1}] = {s[:i+1]}")
            dp[i] = dp[i-1] + 1
            for word in dictionary:
                if word == s[:i+1][-len(word):]:
                    print(f"Found word: {word}")
                    print(f"i: {i}, len(word) = {len(word)}")
                    if i-len(word) == -1:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[i-len(word)])
                    

            print(f"dp[{i}] = {dp[i]}")
                    
        print(dp[-1])
        return dp[-1]
    
sol=Solution()
s = "leetscode"
dictionary = ["leet","code","leetcode"]

s = "sayhelloworld"
dictionary = ["hello","world"]

s = "sayhelhellothisworld"
dictionary = ["hello","world"]

s = "okalamove"
dictionary = ["a","o"]

s = "kevlplxozaizdhxoimmraiakbak"
dictionary = ["yv","bmab","hv","bnsll","mra","jjqf","g","aiyzi","ip","pfctr","flr","ybbcl","biu","ke","lpl","iak","pirua","ilhqd","zdhx","fux","xaw","pdfvt","xf","t","wq","r","cgmud","aokas","xv","jf","cyys","wcaz","rvegf","ysg","xo","uwb","lw","okgk","vbmi","v","mvo","fxyx","ad","e"]

# s = "xhgwxsousikvzrabdxnhhztikglphjzpewwspxqdrdbdgobpmk"
# dictionary = ["xhgwxsousikvzrabdxnhhztikglphjzpewwspxqdrdbdgobpmk","xhgwxso"]
sol.minExtraChar(s, dictionary)
            