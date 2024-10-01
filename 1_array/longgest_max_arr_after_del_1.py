class Solution:
    # def longestSubarray(self, nums: list[int]) -> int:
    #     accu = []
    #     for i in nums:
    #         if i == 0 :
    #             accu.append(0)
    #         else:
    #             if  len(accu) == 0 or accu[len(accu)-1] == 0 :
    #                 accu.append(1)
    #             else: 
    #                 accu[len(accu)-1] += 1
    #     print("accu: ", accu)
    #     new_arr = [accu[0]]
    #     if len(accu) == 1:
    #         if accu[0] != 0:
    #             return accu[0]-1
    #     for i in range(1, len(accu)):
    #         if accu[i] == 0 :
    #             new_arr.append(  accu[i-1] )
    #         if accu[i] != 0:
    #             # if len(new_arr) == 0:
    #             #     new_arr.append(accu[i])
    #             # else:
    #             new_arr.append( new_arr[len(new_arr)-1] + accu[i] )
    #     return max(new_arr)
    def longestSubarray(self, A):
        k = 1
        i = 0
        for j in range(len(A)):
            k -= A[j] == 0
            print("k: ",k)
            if k < 0:
                k += A[i] == 0
                i += 1
                print("k : ", k, ", i: ", i)
        return j - i

s = Solution()
a = [1,0]
# a = [0]
# a = [1,1,1]
# a = [0,0,0]
# a=[0,1]
a = [1, 0, 0, 1,1,1 ,0 ,1,1 ] # 5
# a = [1,1,1, 0, 0, 1,1, 0 ,1,1,1,1,1, 0, 1,1,1 ,0, 0] # 8
# 3 0 0 2 0 5 0 3 0 0 7

print(s.longestSubarray(a))
# 0 0 3 0 1 0 0 4 0 5 0 6 
# 0 0 3 3 4 1 0 4 4 9 5 11

# 1 0 0 3 0 2 
# 1 1 0 3 3 5

# 3 0 0 2 0 5 0 3 0 0 7
