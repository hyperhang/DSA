class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        def calculate(operator: str, arr: list) -> str:
            if operator == '&':
                return 't' if all(ele == 't' for ele in arr) else 'f'
            elif operator == '|':
                return 't' if any(ele == 't' for ele in arr) else 'f'
            else:  # Assuming '!' operator
                return 'f' if arr[0] == 't' else 't'
                  
        stack = []                
        for c in expression:
            if c != ')':
                stack.append(c)
            else:
                t = stack.pop()
                ar = []
                while t != '(':
                    if t == 't' or t == 'f':
                        ar.append(t)
                    t = stack.pop()
                next = calculate(stack.pop(), ar)
                stack.append(next)
        return True if stack[0] == 't' else False
        # TC: O(n)
        # SC: O(n)
       
sol = Solution()
expression = "&(|(f))" # false
# expression = "|(f,f,f,t)" # true
# expression = "!(&(f,t))"  # true
print(sol.parseBoolExpr(expression))
                    
                    
                
                