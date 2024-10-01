class Solution:
    def shortestPalindrome(self, s: str) -> str:
        lim = 1e9 + 7
        base = 29
        if len(s) == 0 or len(s) == 1:
            return s
        
        prefix = [0]
        for c in s:
            prefix.append( ((prefix[-1]*base)%lim+ ord(c) - 96) % lim )
        suffix = [0]
        power = 1
        for c in s:
            suffix.append( ((ord(c) - 96)*power + suffix[-1]) % lim )
            power = (power*base) % lim
            
        l = 0
        for i in range(len(prefix)):
            if prefix[i] == suffix[i]:
                l = i
        print("Max length: ", l)
        add = s[l:]
        ans = add[::-1] + s
        print(ans)
        

s = Solution()
inp = "aceccecadacceca"
inp = "abcdefghiklm"
inp = "aacecaaa"
inp = "aabcd"
inp = "abcd"
# inp = "aaabcd"
# inp = "aaaabcd"
# inp = "aaaaabcd"
# inp = "aba"
# inp = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
s.shortestPalindrome(inp)

        