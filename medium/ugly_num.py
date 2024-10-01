import bisect

class Solution:
    def find_nearest_less_or_equal(self, arr, x):
        # Find the insertion point for x
        idx = bisect.bisect_right(arr, x)
        
        # If x is greater or equal to all elements in the array
        if idx >= len(arr):
            return None
        # Return the index of the element just greater strictly to x
        return idx 
    
    def nthUglyNumber(self, n: int) -> int:
        ugly_list = [0,1,2,3,4,5,6,8,9]
        if n <=8 :
            return ugly_list[n]
        
        while len(ugly_list) < n+1:
            num = ugly_list[len(ugly_list)-1]
            m = 1e18
            for i in [2,3,5]:
                ni = num//i
                newi = self.find_nearest_less_or_equal(ugly_list, ni)
                newi = ugly_list[newi]*i
                m = min(m, newi)
            ugly_list.append(m)
            
        return ugly_list[len(ugly_list)-1]

sol = Solution()

n = 1
# n = 10
# n = 11
n = 423
n = 1690
print(sol.nthUglyNumber(n))
            
                