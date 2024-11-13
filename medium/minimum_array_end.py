class Solution:
    def minEnd(self, n: int, x: int) -> int:
        start = bin(x)[2:]
        filled = bin(n-1)[2:]
        start = list(start)
        j = len(filled)-1
        print("start:  ", start)
        print("filled: ", filled)
        for i in range(len(start) - 1, -1, -1):
            if start[i] == '0':
                print(f"filled[{j}] = {filled[j]}")
                start[i] = filled[j]
                j -= 1
                if j < 0:
                    break
        print("start join: ", ''.join(start))
        print("filled: ",filled[:j+1] )
        temp = ''.join(start)
        if j >= 0:
            temp = filled[:j+1] + temp
            
        print(temp)
        return int(temp, 2)
                
sol = Solution()
n = 3
x = 1

n = 3
x = 4

print(sol.minEnd(n, x))
        