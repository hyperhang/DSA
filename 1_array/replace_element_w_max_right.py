class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_right = arr[len(arr)-1]
        for i in range(len(arr)-2,-1,-1):
            max_temp = max_right
            if max_temp < arr[i]:
                max_temp = arr[i]
            arr[i] = max_right
            if max_right < max_temp:
                max_right = max_temp
            print(f"max_right: {max_right}, max_temp: {max_temp}")
        arr[len(arr)-1] = -1
        return arr
    
s = Solution()
print(s.replaceElements([17,18,5,4,6,1]))