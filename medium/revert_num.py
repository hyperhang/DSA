class Solution:
    def reverse(self, x: int) -> int:
        # -2147483648 -> 2147483647
        bottom_lim = '2147483648'
        top_lim = '2147483647'
        reverted_str = ''
        original_num = x
        x = abs(x)
        # We need to use string because 64 bit number is not supported then the reverted_num can be out of range.
        x = str(x)
        for i in x:
            reverted_str = i + reverted_str
        print(reverted_str)
        if original_num < 0:
            if len(reverted_str) < len(bottom_lim) or  reverted_str <= bottom_lim:
                return -int(reverted_str)
        else:
            if len(reverted_str) < len(top_lim) or reverted_str <= top_lim:
                return int(reverted_str)
        return 0
                

s = Solution()
# print(s.reverse(-2147483648))
# print(s.reverse(-2183648))
print(s.reverse(1534236469))