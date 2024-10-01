class Solution:
    def longestPalindrome(self, s: str) -> str:
        # abeiwfkfwbeweb
        palindrome = []
        for _ in range(len(s)):
            palindrome.append([0 for _ in range(len(s))])

        def check_palindrome(i, j):
            if (i+1==j or i+2 == j) and s[i]==s[j]:
                palindrome[i][j] = 1
                # print("palindrome: ", s[i:j+1])
                return 1
            if i+3 <= j:
                if palindrome[i+1][j-1] and s[i] == s[j]:
                    # print("--palindrome: ", s[i:j+1])
                    palindrome[i][j] = 1
                    return 1
            return 0
        
        window_size = 2
        start_i = 0
        end_i = 0
        while window_size <= len(s):
            i = 0
            while i+window_size-1 < len(s):
                res = check_palindrome(i, i+window_size-1)
                if res and  window_size > end_i - start_i + 1:
                    start_i = i
                    end_i = i+window_size-1
                i = i + 1
            window_size += 1
        # print("Palindrome:\n")
        # for i in range(len(palindrome)):
        #     print(palindrome[i])
        if end_i-start_i>0:
            return s[start_i:end_i+1]
        return s[0]

s = Solution()
# print(s.longestPalindrome('fjiwef'))
# print(s.longestPalindrome('abeiwfkfwbewebwu'))
# print(s.longestPalindrome('babad'))
print(s.longestPalindrome('cbb'))
print(s.longestPalindrome('bb'))