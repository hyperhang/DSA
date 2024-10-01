import heapq
from collections import defaultdict

# Dijkstra
class Solution:
    def maxProbability(self, n: int, edges: list[list], succProb: list[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        max_prob = [0.0] * n
        max_prob[start] = 1.0
        
        pq = [(-1.0, start)]    
        while pq:
            print(f"------------\ncandidates: ", pq)
            cur_prob, cur_node = heapq.heappop(pq)
            print(f"selected node: ", cur_node, "prb from start to node: ", cur_prob)
            if cur_node == end:
                return -cur_prob
            for nxt_node, path_prob in graph[cur_node]:
                print("child: ", nxt_node, path_prob)
                if -cur_prob * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = -cur_prob * path_prob
                    heapq.heappush(pq, (-max_prob[nxt_node], nxt_node))
            print("Updated candidates: ", pq)
        return 0.0


# # Bellman-ford
# class Solution:
#     def maxProbability(self, n: int, edges: list[list], succProb: list[float], start: int, end: int) -> float:
#         max_prob = [0] * n
#         max_prob[start] = 1
        
#         for i in range(n - 1):
#             # If there is no larger probability found during an entire round of updates,
#             # stop the update process.
#             has_update = 0
#             for j in range(len(edges)):
#                 u, v = edges[j]
#                 path_prob = succProb[j]
#                 if max_prob[u] * path_prob > max_prob[v]:
#                     max_prob[v] = max_prob[u] * path_prob
#                     has_update = 1 
#                 if max_prob[v] * path_prob > max_prob[u]:
#                     max_prob[u] = max_prob[v] * path_prob
#                     has_update = 1
#             if not has_update:
#                 break
        
#         return max_prob[end]

# # shortest path alg
# from collections import deque 
# class Solution:
#     def maxProbability(self, n: int, edges: list[list], succProb: list[float], start: int, end: int) -> float:
#         graph = defaultdict(list)
#         for i, (a, b) in enumerate(edges):
#             graph[a].append([b, succProb[i]])
#             graph[b].append([a, succProb[i]])
            
#         max_prob = [0.0] * n    
#         max_prob[start] = 1.0
        
#         queue = deque([start])
#         while queue:
#             cur_node = queue.popleft()
#             for nxt_node, path_prob in graph[cur_node]:

#                 # Only update max_prob[nxt_node] if the current path increases
#                 # the probability of reach nxt_node.
#                 if max_prob[cur_node] * path_prob > max_prob[nxt_node]:
#                     max_prob[nxt_node] = max_prob[cur_node] * path_prob
#                     queue.append(nxt_node)
                    
#         return max_prob[end]



s = Solution()

# n = 5
# edges = [  [2,3],[ 1,2], [3,4],[1,3], [1,4], [0,1], [2,4], [0,4], [0,2]]
# succProb = [0.06, 0.26,  0.49,  0.25,  0.2,  0.64,  0.23,  0.21,   0.77]
# start= 0
# end= 3
# print(s.maxProbability(n, edges, succProb, start, end))         



n = 5
edges =   [[0,1] , [0,2], [0,4], [2, 1], [2, 4]]
succProb = [0.64,   0.77,  0.21,  0.91,   0.44]
start = 0
end = 3

print(s.maxProbability(n, edges, succProb, start, end))    