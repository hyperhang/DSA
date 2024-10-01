from typing import List
from collections import defaultdict
import heapq

class Solution:
    INF = int(2e9)
    LIM_EDGE = int(1e7)
    
    def modifiedGraphEdges(self, n: int, edges: List[List[int]],source: int,destination: int, target: int) -> List[List[int]]:
        
        def run_dijsktra(edges, graph):
            # O(): n+m.log(n) : n (# of nodes), m (# of edges)
            min_path = [self.INF] * n
            min_path[source] = 0
            hq = [[0, source]]
            
            while len(hq) !=0 :
                next_w, next_node = heapq.heappop(hq)
                if next_node == destination:
                    return next_w
                for child in graph[next_node]:
                    child_edge, child_node = child
                    if child_edge + next_w < min_path[child_node]:
                        min_path[child_node] =  child_edge + next_w 
                        heapq.heappush(hq, [ min_path[child_node], child_node])
            return self.INF


        graph = defaultdict(list)
        for e in edges:
            if e[2] != -1: # ignore -1 weight edge
                graph[e[0]].append([e[2], e[1]]) # weight, node
                graph[e[1]].append([e[2], e[0]])

        # 1st, check min path using Dijkstra (ignore all -1 edges)  :
        first_min_path = run_dijsktra(edges)  
        if  first_min_path < target:
            return []
        
        is_matches_target = False
        
        if first_min_path == target:
            is_matches_target = True
        for e in edges:
            if e[2] < 0: # ignore positive edge weight
                if is_matches_target: # if target is reached, fill all other edges to INF to make sure min path stays the same
                    e[2] = self.LIM_EDGE
                    # graph[e[0]] -> update weight in graph
                    continue
                else:
                    e[2] =1
                    # update weight in graph
                    
                current_min_path = run_dijsktra(edges)
                if current_min_path <= target:
                    e[2] = e[2] + target - current_min_path
                    # update weight in graph
                    is_matches_target = True
        return edges        
                
            
# Explain O(): 
# Dijkstra: O(n+m.log(n))
# m*(n+m.log(n)) = m^2.log(n) + m.n ,  n<=10^2, m<=n^2=10^4, Binary heap is used
#  -> Time exceed because > 10^8
# -> If use heap with Fibonaci heap then O() is okay, O() = m*(m+n.log(n)) = m^2 + m*n*log(n)









s = Solution()

# n = 5
# edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
# source = 0
# destination = 1
# target = 5


# n = 3
# edges = [[0,1,-1],[0,2,5]]
# source = 0
# destination = 2
# target = 6


# n = 4
# edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]]
# source = 0
# destination = 2
# target = 6



# n = 4
# edges = [[0,1,-1],[1,2,-1],[3,1,-1],[3,0,2],[0,2,5]]
# source = 2
# destination = 3
# target = 8 # expect: []


n =4
edges =[[3,0,-1],[1,2,-1],[2,3,-1],[1,3,9],[2,0,5]]
source =0
destination =1
target =7

print(s.modifiedGraphEdges(n, edges, source, destination, target))

        
        