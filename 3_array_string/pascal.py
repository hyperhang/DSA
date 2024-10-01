class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return[[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        mat = [[1],[1,1]]
        for i in range(2, numRows+1):
            pre_row = mat[len(mat)-1]
            print("\npre_row: ", pre_row)
            row = [1]
            for j in range(1,len(pre_row)):
                row.append(pre_row[j]+pre_row[j-1])
            row.append(1)
            print("row:     ", row)
            mat.append(row)
            print("mat:     ", mat)
        print(mat)
                
s = Solution()
s.generate(5)