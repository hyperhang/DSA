from collections import defaultdict
import heapq
class Solution:
    result = 0
    def maxProbability(self, n: int, edges: list[list], succProb: list, start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(succProb)):
            graph[edges[i][0]].append([succProb[i], edges[i][1]])
            graph[edges[i][1]].append([succProb[i], edges[i][0]])
        print("Graph: ", graph)
        max_prob = [0]*n
        max_prob[start_node] = 1
        
        hq = [[-1, start_node]]
        
        while len(hq) != 0:
            next_prob, next_node = heapq.heappop(hq)
            next_prob = -next_prob
            if next_node == end_node:
                return next_prob
                
            for child_edge in graph[next_node]:
                prob_c, node_c = child_edge[0], child_edge[1]
                if prob_c*max_prob[next_node] > max_prob[node_c]:
                    max_prob[node_c] = prob_c*max_prob[next_node]
                    heapq.heappush(hq, [-max_prob[node_c], node_c])
        return 0
    
s = Solution()
# n = 3
# edges = [[0,1],[1,2],[0,2]]
# succProb = [0.5,0.5,0.2]
# start = 0
# end = 2

# n = 3
# edges = [[0,1],[1,2],[0,2]]
# succProb = [0.5,0.5,0.3]
# start = 0
# end = 2

n = 3
edges = [[0,1]]
succProb = [0.5]
start = 0
end = 2

print(s.maxProbability(n,edges,succProb, start, end))        