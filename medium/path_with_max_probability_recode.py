from collections import defaultdict
import heapq
class Solution:
    result = 0
    def maxProbability(self, n: int, edges: list[list], succProb: list, start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for idx, e in enumerate(edges):
            graph[e[0]].append([e[1], succProb[idx]])
            graph[e[1]].append([e[0], succProb[idx]])
        print(graph)
        
        max_prob = [0 for _ in range(n)]
        max_prob[start_node] = 1
        
        candidates = [[-1, start_node]]
        
        heapq.heapify(candidates)
        
        def find_max_prob(candidates):
            print("---------\ncandidates: ", candidates)
            if len(candidates) == 0:
                return
            _next_node_prob, _next_node = heapq.heappop(candidates)
            _next_node_prob = -_next_node_prob
            print(f"next_node: {_next_node}, prob: {_next_node_prob}")
            if _next_node == end_node:
                self.result = _next_node_prob
                return 
            for child, child_prob in graph[_next_node]:
                print(f"child: {child} - {child_prob}")
                _prob = child_prob * max_prob[_next_node]
                if _prob > max_prob[child]:
                    max_prob[child] = _prob
                    heapq.heappush(candidates, [-_prob, child]) # Here we add new can, but if the candidate already exists: How to update the old candidate which its max prob in the candidates heap.
                print("updated candidates: ", candidates)
            find_max_prob(candidates)
            return
        
        find_max_prob(candidates)
        
        return self.result
                

              
 
s = Solution()

# n = 3
# edges = [[0,1],[1,2],[0,2]]
# succProb = [0.5,0.5,0.2]
# start = 0
# end = 2
# print(s.maxProbability(n, edges, succProb, start, end))         


# n = 3
# edges = [[0,1],[1,2],[0,2]]
# succProb = [0.5,0.5,0.3]
# start = 0
# end = 2       
# print(s.maxProbability(n, edges, succProb, start, end))         

# n = 3
# edges = [[0,1]]
# succProb = [0.5]
# start = 0
# end = 2

# print(s.maxProbability(n, edges, succProb, start, end))         


n = 4
edges =   [[0,1] , [0,2], [0,4], [2, 1], [2, 4]]
succProb = [0.64,   0.77,  0.21,  0.91,   0.44]
start = 0
end = 3

print(s.maxProbability(n, edges, succProb, start, end))    