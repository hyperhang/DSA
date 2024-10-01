class Solution:
    kth = 0
    def findKthNumber(self, n: int, k: int) -> int:
        
        def count_number(n1, n2):
            if n1 == 0:
                return [0,0]
            c=1
            while n1*10 <= n:
                n1 = n1*10
                n2 = n2*10
                if n2-1 <= n:
                    c += n2-n1
                else:
                    c += n-n1+1
                    break
            return c
                
        def check_next(cur_num: int, k: int):
            for i in range(10):
                c= count_number(cur_num + i, cur_num + i + 1)
                print(f"\n---\ncount_number({cur_num +i}, {cur_num+i+1}) = {c}")
                print(f"k = {k}")
                print(f"c vs k : {c}, {k} ")
                if c < k :
                    k = k - c
                    continue
                else:
                    if k == 1:
                        self.kth = cur_num+i
                        return
                    cur_num = ( cur_num +  i) * 10
                    k -= 1
                    
                    check_next(cur_num, k)
                    break
        
        check_next(0, k)
        ans = self.kth
        print(ans)
        return ans

s = Solution()

n,k = 13, 2  # 10

n = 30
k = 28 # 7

n = 681692778
k = 351251360 # 416126219

# n,k=1,1   # 1

n,k=100,90 # 9
# n,k = 4,3 # 3

# n,k = 10,2 # 19

s.findKthNumber(n, k)
                