class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ''
        for c in s:
            c = ord(c) - 96
            num = num + str(c)
        print("num: ", num)
        
        def transform(num: str):
            su = 0
            for i in num:
                su += int(i)
            print("transform: ", su)
            return str(su)
        
        res = num
        for i in range(k):
            res = transform(res)
        
        print(int(res))
        return int(res)

sol = Solution()

s = "zbax"
k = 2

s = "iiii"
k = 1

s = "leetcode"
k = 2

s = "i"
k = 1
print(sol.getLucky(s, k))