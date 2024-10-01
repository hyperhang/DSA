class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        arr = []
        carry = 0
        if digits[len(digits)-1] == 9 :
            carry = 1
            arr.append(0)
        else:
            for idx, ele in enumerate(digits):
                if idx != len(digits)-1 :
                    arr.append(ele)
                else: 
                    arr.append(ele+1)
            return arr
        if len(digits) == 1:
            return [1,0]
        for i in range(len(digits)-2, -1,-1):
            if carry:
                if digits[i]+1 == 10:
                    arr.append(0)
                    carry = 1
                else:
                    arr.append(digits[i]+1)
                    carry = 0
            else:
                arr.append(digits[i])
        if carry:
            arr.append(1)
        res = []
        print(arr)
        for i in range(len(arr)-1, -1, -1):
            res.append(arr[i])
        print(res)
        return res
                
s = Solution()
# a = [1,2,3]
# a = [4,3,2,1]
# a= [9]
# a = [8]
a = [9,9,9]
print(s.plusOne(a))        