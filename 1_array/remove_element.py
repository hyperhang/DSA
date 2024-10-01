class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        # while i<j and i < len(nums):
        # j là pt cuối cùng, duyệt j->0 sao cho đến khi khác val
        while j>=0:
            if nums[j] == val:
                j -= 1
                print("j : ", j)

            else:
                break
        print("j : ", j)
        if j <= 0:
            print(j+1)
            return j+1
        # i là pt đầu tiên, duyệt i-> j \ tới khi bằng val thì đổi chỗ nums[i] với nums[j]
        while i < j and i < len(nums):
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            else:
                i += 1
            print(f"i: {i}, j: {j}")
            while j>0:
                if nums[j] == val:
                    j -= 1   
                else:
                    break
        print(nums)
        end = len(nums) - 1
        while nums[end] == val:
            end -= 1
        print(end+1)
        return end + 1      
            
s = Solution()
# a = [2,2,2,3]
a = [2,2,2,2]
# a = [3,2,2,3]
# a = [0,1,2,2,3,0,4,2]
s.removeElement(a, 2)