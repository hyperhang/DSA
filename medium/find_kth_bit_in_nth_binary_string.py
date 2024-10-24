class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # 2(2(2x+1)+1)+1
        def invert(s: str)->str:
            t = ''
            for c in s:
                t += '1' if c == '0' else '0'
            return t
        
        s = '0'
        for i in range(2,n+1):
            s = s+'1'+invert(s)[::-1]
        print("res: ", s)
        return s[k-1]

sol = Solution()
n = 3
k = 1
n, k = 4, 11
print(sol.findKthBit(n, k))