class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        post = {
            'I': ['V', 'X'],
            'X': ['L', 'C'],
            'C': ['D', 'M']
        }
        i = 0
        while i < len(s):
            print("i: ", i, s[i])
            if i+1 < len(s) :
                cur = s[i]
                if cur in post and s[i+1] in post[cur]:
                    num += val[s[i:i+2]]
                    print(f"value: {val[s[i:i+2]]}")
                    i += 1
                else:
                    num += val[s[i]]
                    print(f"val: {val[s[i]]}")
            else:
                num += val[s[i]]
                print(f"val: {val[s[i]]}")
            i += 1
        return num
            
sol = Solution()
s = 'III'
# s = 'LVIII'
# s = "MCMXCIV"
print(sol.romanToInt(s))
"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

MCMX CIV
1000-100-1000-10-100-1-5
1000-900-90-4

LVIII
50-5-1-1-1

I: V, X -> 4, 9
X: L, C -> 40, 90
C: D, M -> 400, 900
"""