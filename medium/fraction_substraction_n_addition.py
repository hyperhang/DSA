from fractions import Fraction

# class Solution:
#     def fractionAddition(self, expression: str) -> str:
#         signs = []
#         sign_idxs = []
#         fractions = []
            
#         for i, exp in enumerate(expression):
#             if exp == "-" or exp == "+":
#                 signs.append(exp)
#                 sign_idxs.append(i)
#         if len(sign_idxs) == 0:
#             return expression
        
#         if expression[0] != '-':
#             fractions.append(expression[:sign_idxs[0]])
#         for i in range(len(sign_idxs)-1):
#             fractions.append(expression[sign_idxs[i]+1:sign_idxs[i+1]])
#         fractions.append(expression[sign_idxs[-1]+1:])
            
#         def str_to_fraction(fraction: str):
#             idx = fraction.find("/")
#             return Fraction(int(fraction[:idx]), int(fraction[idx+1:]))
        
#         print("signs: ", signs)
#         print("fractions: ", fractions)
#         su = Fraction(0,1)
#         if expression[0] != '-':
#             signs.insert(0, '+')
#         for i in range(len(signs)):
#             if signs[i] == '-':
#                 su = su - str_to_fraction(fractions[i])
#             if signs[i] == '+':
#                 su = su + str_to_fraction(fractions[i])
#         print(su.as_integer_ratio)  
#         t = su.as_integer_ratio()
#         n, d = t[0], t[1]
#         print(n, d)
#         return f"{n}/{d}"
            
            
            

# class Solution:
#     def fractionAddition(self, expression: str) -> str:
#         sign = '+'
#         num1, num2 = '0', '1'
#         numerator = False
#         su = Fraction(0,1)
#         if expression[0] != '-':
#             expression = '+' + expression
        # for c in expression:
        #     if c == '-' or c == '+':
        #         t = Fraction(int(sign+num1), int(num2))
        #         print("num: ", t)
        #         su += t
        #         num1, num2 = '', ''
        #         numerator = not numerator
        #     if c == '-':
        #         sign = '-'
        #     elif c == '+':
        #         sign = '+'
        #     elif c == '/':
        #         numerator = not numerator
        #     else:
        #         if numerator:
        #             num1 += c
        #         else:
        #             num2 += c

        # t = Fraction(int(sign+num1), int(num2))
        # print("num: ", t)
        # su += t
        # print(su)       
        # return f"{su.numerator}/{su.denominator}"


class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0] != '-':
            expression = '+' + expression
        new_exp = ''
        for c in expression:
            if c == '-' or c == '+':
                new_exp += ','
            new_exp += c
            
        fractions = new_exp.split(',')

        def str_to_fraction(fraction: str):
            idx = fraction.find("/")
            return Fraction(int(fraction[:idx]), int(fraction[idx+1:]))
        
        su = Fraction(0, 1)
        for num in fractions[1:]:
            su += str_to_fraction(num)

        return f"{su.numerator}/{su.denominator}"
            
        
s = Solution()
expression = "-1/2+1/2"
# expression = "1/3-1/2"
# expression = "-4/5"
# expression = "-1/2+1/2-1/3"
print(s.fractionAddition(expression))                
        