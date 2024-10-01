# class Solution:
#     def removeStones(self, stones: list[list]) -> int:
#         last_key = 1
#         groups = { last_key: [set([stones[0][0]]), set([stones[0][1]]) ] } # list of list Ox, Oy - 0: set() of Ox, 1: set of O(y)
#         for stone in stones:
#             x, y = stone[0], stone[1]
#             merge_groups_keys = []
#             for key, group in groups.items(): 
#                 Ox, Oy = group[0], group[1]
#                 if x in Ox or y in Oy:
#                     merge_groups_keys.append(key)
#             if len(merge_groups_keys) == 0:
#                 # need a new group
#                 last_key += 1
#                 groups[last_key] = [ set([x]) , set([y]) ]    
#             else:
#                 merged_group_key = merge_groups_keys[0]
#                 merge_groups_value = [set(), set()]
#                 for k in merge_groups_keys:
#                     Ox_set = groups[k][0]
#                     Oy_set = groups[k][1]
#                     merge_groups_value[0] = merge_groups_value[0].union(Ox_set)
#                     merge_groups_value[1] = merge_groups_value[1].union(Oy_set)
#                     del groups[k]
#                 merge_groups_value[0].add(x)
#                 merge_groups_value[1].add(y)
                
#                 groups[merged_group_key] = merge_groups_value
                
#             print("Updated groups: ", groups)
                
#         print("GROUP: ")
#         for g in groups:
#             print(g)
#         return len(stones) - len(groups)
    
    
class Solution:
    def removeStones(self, points):
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)

        for i, j in points:
            union(i, ~j)
        print("UF: ", UF)
        return len(points) - len({find(x) for x in UF})
    
    
    
s = Solution()
# st = [[0,0],[0,2],[1,1],[2,0],[2,2]] # 3
st = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]] # 5
# st = [[0,0]] # 0
# st = [[0,1],[1,0],[1,1]]  # output: 2
print( "RESULT: ", s.removeStones(st))