class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        j = len(arr) - 1
        print(i,j)
        # tim vi tri cuoi cung con trong day, dem xem co bao nhieu so 0 vẫn còn đc giữ 
        flag = False
        while i < j :
            if arr[i] == 0 and i+1 == j:
                flag = True # -> cần duplicate số 0 ở cuối.
                break
            if arr[i] == 0:
                j -= 1
            i += 1
            print(i, j)
        
        print("flag: ", flag)
        # tat ca vi tri sau i deu bi loai bo, giả sử là None.
        start = i
        for k in range(i+1, len(arr)):
            arr[k] = None
        print(arr, len(arr))
        # duyệt từ phải qua trái, kéo dần phần tử ở cuối cùng qua bên phải cùng , gặp 0 thì thêm 1 số 0 nữa.
        # Đặc biệt lưu ý: flag = False thì ko duplicate số 0 cuối cùng, flag = True thì dup số 0 cuối cùng.
        end = len(arr) - 1
        if arr[start] == 0 :
            arr[end] = arr[start]
            if flag:
                arr[end-1] = arr[start]
                end -= 1
            start -= 1
            end -= 1
        print(arr)
        while start >= 0 :
            print(f"\nend:{end}, start: {start}")
            print(f"end_ele: {arr[end]}, start_ele: {arr[start]}")
            print(arr)
            arr[end] = arr[start]
            end = end - 1

            if arr[start] == 0:
                arr[end] = 0
                end -= 1
            # print(f"-- end: {end}, start: {start}")
            # arr[start] = None
            start -= 1
        print(arr)
        
s = Solution()
a = [1,5,2,0,6,8,0,   6,0]
# [1, 4, 1, 0, 0, 8, 9, 8, 0,   0, 3]
s.duplicateZeros(a)
