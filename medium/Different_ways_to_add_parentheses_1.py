from typing import List
from itertools import product
from operator import add, sub, mul
import re

class Solution:
    count = 0
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def cross_product(l1: list[int], l2: list[int], operator: str) -> list:
            op_map = {'+': add, '-': sub, '*': mul}
            op_func = op_map.get(operator, mul)  # Default to multiplication if operator is invalid
            return [op_func(i, j) for i, j in product(l1, l2)]          
                          
        operators = [c for c in expression if c in '+-*']
        nums = re.split(r'[+\-*]', expression)
        num_list = [int(n) for n in nums]
        
        n = len(num_list)
        dp = [[1 for i in range(n+1)] for _ in range(n)]
        # dp[i][j]: tap gia tri cua cac bieu thuc bat dau tai i, co do dai la j
        for i in range(n):
            dp[i][1] = [num_list[i]]
        print("init: ")
        print(dp)
        for j in range(2,n+1):
            for i in range( n+1-j):
                t = []
                for k in range(1, j):
                    x = [dp[i][k]] if type(dp[i][k]) == int else dp[i][k]
                    y = [dp[i+k][j-k]] if type(dp[i+k][j-k]) == int else dp[i+k][j-k]
                    self.count += 1
                    t = t + cross_product(x, y, operators[i+k-1])
                    
                dp[i][j] = t
                print(f"dp[{i}][{j}] = ", dp[i][j])
                
        print(dp[0][n])
        print("length res: ", len(dp[0][n]))
        print("count operators: ", self.count)
        
        return dp[0][n]

s = Solution()
expression = "2*3-4*5"
expression = "2-1-1"
# expression = "9+4*5*7-9+22*63-2+3*89-52"
# expression = "9+4*5*7-9+22*63-2+3*89-52"
"""
1: 1
2: 
"""
s.diffWaysToCompute(expression)