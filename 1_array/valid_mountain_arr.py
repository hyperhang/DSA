class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr)<3:
            return False
        diff = []
        for i in range(1, len(arr)):
            temp = arr[i]-arr[i-1]
            if temp < 0:
                diff.append(-1)
            elif temp == 0:
                return False
            else:
                diff.append(1)
        separate_count = 0
        print("diff: ", diff)
        for i in range(1, len(diff)):
            if diff[i] != diff[i-1]:
                separate_count += 1
                if separate_count > 1:
                    return False

        if not (diff[0] == 1 and diff[len(diff)-1] == -1):
            return False
        return True 
            
            
        
s = Solution()
print(s.validMountainArray([0,1,2,3,4,5,6,7,8,9]))