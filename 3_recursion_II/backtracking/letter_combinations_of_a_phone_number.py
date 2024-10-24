from typing import List


# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         phone = {'2': 'abc',
#                  '3': 'def',
#                  '4': 'ghi',
#                  '5': 'jkl',
#                  '6': 'mno',
#                  '7': 'pqrs',
#                  '8': 'tuv',
#                  '9': 'wxyz'}
        
#         all = []
        
#         def gen(current: str, idx:int):
#             if idx == len(digits):
#                 all.append(current)
#                 return
#             for char in phone[digits[idx]]:
#                 gen(current+char, idx+1) # TC: string concatenation is O(N), N: string's length
#         gen('', 0)
#         if len(digits) == 0:
#             return []
#         return all
#         # TC: (4N)^N, N: string length. xxxxxxxxxxxx
          # SC: ()


# Backtracking approach:
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0:
            return []

        # Map all the digits to their corresponding letters
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int, path: list):
            print("path: ", path)
            if len(path) == len(digits):
                combinations.append("".join(path))
                return  # Backtrack

            for letter in letters[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations
        
sol = Solution()
digits = '23'
# digits = '2'
# digits = ''
print(sol.letterCombinations(digits))