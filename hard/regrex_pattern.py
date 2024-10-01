class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
# . : any single char
# *: 0 or more of preceding element
# s = "aab", p = “qc*a*b"
# s = "mississippi", p = "mis*is*p*."

        # find the first dot or star in the p string
        # if * is found at index i, check if 
        # p[:i] has length == 1 and 
        # p[:i+1]...
        # if . is found, 