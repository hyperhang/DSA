from typing import List
import bisect

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n = 1001
        is_prime = [1]*n
        i = 2
        primes = []
        while i < n:
            if is_prime[i]:
                primes.append(i)
                j = 2
                while i*j < n:
                    is_prime[i*j] = 0
                    j += 1
            i += 1
                
        def find_biggest_prime(lim: int) -> int:
            idx = bisect.bisect_left(primes,lim)
            if idx == 0:
                return 0
            return primes[idx-1]
            
        if find_biggest_prime(nums[0]):
            new_ar = [nums[0]-find_biggest_prime(nums[0])]
        else:
            new_ar = [nums[0]]
        for ele in nums[1:]:
            tem = find_biggest_prime(ele - new_ar[-1])
            if tem:
                new_ar.append(ele - tem)
            else:
                new_ar.append(ele)
                if new_ar[-1] <= new_ar[-2]:
                    return False
        return True    
    # TC: O(N*log N)
    # SC: O(N)
         
sol = Solution()
nums = [4,9,6,10]
nums = [6,8,11,12]
# nums = [5,8,3]
nums = [998,2]
print(sol.primeSubOperation(nums))