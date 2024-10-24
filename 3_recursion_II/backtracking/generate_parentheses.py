from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # ()
        """
        1: ()
        2: ()(), (())
        3: (2) :  (()()), ((()))
            1.2: () ()(), ()(())
            2.1: () ()(), (())()
        """
        dp = {}
        def gen(n:int):
            if n in dp:
                return dp[n]
            if n == 1:
                dp[1] = set(['()'])
                return dp[1]
            if n == 2 :
                dp[2] =  set(['()()', '(())'])
                return dp[2]
            
            ans = set()
            l1 = gen(n-1)
            for ele in l1:
                ans.add(f"({ele})")
            for i in range(1,n):
                li = gen(i)
                li_ = gen(n-i)
                for i in li:
                    for j in li_:
                        ans.add(i+j)
            dp[n] = ans
            return dp[n]
        
        return gen(n)
        
sol = Solution()
n = 3
n = 1
n = 2
n = 4
print(sol.generateParenthesis(n))
        
        