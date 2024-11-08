class Solution:
    def getMaximumXor(self, nums:list, maximumBit: int):
        tem = 2**maximumBit-1
        cur_xor = nums[0]
        ans = [cur_xor^tem]
        print(f"cur_xor: {cur_xor}, k = {ans[-1]}" )
        for ele in nums[1:]:
            cur_xor ^= ele
            ans.append(cur_xor^tem)
            print(f"cur_xor: {cur_xor}, k = {ans[-1]}" )
        print(ans)
        return ans[::-1]
            
sol = Solution()
nums = [0,1,1,3]
maximumBit = 2       

nums = [2,3,4,7]
maximumBit = 3

nums = [0,1,2,2,5,7]
maximumBit = 3
sol.getMaximumXor(nums, maximumBit)            
            

"""
111

010 ? 111 => 101
10010 010 ? 111 => 10010 101
? : XOR
"""