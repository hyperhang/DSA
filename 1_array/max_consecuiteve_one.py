# 4 0 3 0 6  0 1 0 0 3 0 0 0 0 6 
#   5 8 4 10 7 8 2 1 4 4 1 1 1 7

# 1 0 2 0  0
#   2 4 3  1

   
# 1 1 1 0 1 0 0 1 1 1 1 0 0 0 1 1 1
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        i = 0
        max_con_one = 0
        accumulated_one = []
        while i < len(nums):
            if nums[i] == 0 :
                accumulated_one.append(0)
            if nums[i] == 1 :
                if nums[i-1] == 0 or i==0:
                    accumulated_one.append(1)
                else:
                    accumulated_one[len(accumulated_one)-1] += 1
            i+=1
        print("accumulated one: ", accumulated_one)
        added_arr = [0]
        if len(accumulated_one) == 1 :
            if accumulated_one[0] == 0:
                return 1
            else:
                return accumulated_one[0]
        if accumulated_one[0] == 0:
            added_arr = [1]
            
        for idx, ele in enumerate(accumulated_one):
            if idx == 0:
                continue
            if ele == 0 :
                if idx - 1 >= 0:
                    added_arr.append(accumulated_one[idx-1]+1)
                else:
                    added_arr.append(1)     
            else:
                added_arr.append(ele + added_arr[len(added_arr)-1])
        return max(added_arr)
                
s = Solution()
# a = [1,1,1,1, 0, 1,1,1, 0, 1,1,1,1,1,1,  0, 1, 0, 0, 1,1,1, 0, 0 ,0 ,0, 1,1,1,1,1,1 ]
a = [0,1,1,1]
print(s.findMaxConsecutiveOnes(a))