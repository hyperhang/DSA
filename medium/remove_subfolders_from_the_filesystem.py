from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        cur = folder[0]
        ans = [cur]
        def check(s1:str, s2:str):
            if s1 == s2[:len(s1)] and s2[len(s1)] == '/':
                return True
            return False
        for ele in folder[1:]:
            if not check(cur, ele):
                ans.append(ele)
                cur = ele
        return ans
    
sol = Solution()
folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# folder = ["/a","/a/b/c","/a/b/d"]
# folder = ["/a/b/c","/a/b/ca","/a/b/d"]
print(sol.removeSubfolders(folder))
            