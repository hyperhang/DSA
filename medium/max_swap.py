class Solution:
    def maximumSwap(self, num: int) -> int:
        # 63424525
        # 
        # 65544322
        
        # 
        # 65424523
        digits = list(str(num))
        sorted_digit = sorted(digits, reverse=True)
        print("sorted: ", sorted_digit)
        i = 0
        for i in range(len(digits)):
            if digits[i] != sorted_digit[i]:
                break
        if i == len(digits):
            return num
        t1 = sorted_digit[i]
        t2 = digits[i]
        digits[i] = sorted_digit[i]
        j = len(digits) - 1
        while digits[j] != t1:
            j -= 1
        digits[j] = t2
        print("final: ", digits)
        return int(''.join(digits))
        
sol = Solution()
num = 63424525
# num = 2736
# num = 9973
print(sol.maximumSwap(num))
        
        

