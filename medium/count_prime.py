class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True]*(n+1)
        primes[0] = False
        primes[1] = False
        primes[2] = True
        
        i = 2
        while i < n:
            if primes[i] == True:
                for k in range(2,n//i+1):
                    primes[i*k] = False
            i += 1
        c=0
        for p in range(n+1):
            if primes[p]:
                c+= 1
            print(f" {p} : {primes[p]}")
        print("res : ", c)
        
sol = Solution()
sol.countPrimes(15)