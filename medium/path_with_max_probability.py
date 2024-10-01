# Dijkstra's algorithm

class Solution:
    max_probability = 0
    
    def get_pair(self, n1, n2) -> str:
        return f"{min(n1, n2)}-{max(n1, n2)}"
    
    def maxProbability(self, n: int, edges: list[list], succProb: list, start_node: int, end_node: int) -> float:
        get_child = dict()
        get_succ_prob = dict()
        for idx, edge in enumerate(edges):
            n1, n2 = edge[0], edge[1]
            get_succ_prob[f"{min(n1, n2)}-{max(n1, n2)}"] = succProb[idx]
            if n1 in get_child:
                get_child[n1].append(n2)
            else:
                get_child[n1] = [n2]
                
            if n2 in get_child:
                get_child[n2].append(n1)
            else:
                get_child[n2] = [n1]
        
        for k, v in get_child.items():
            print(k,' : ', v)
        for k, v in get_succ_prob.items():
            print(k,' : ', v)
    
    
        visited = set([start_node])
        get_max_prob = {start_node: 1} # get_max_prob[x] = y, where x: node number, y: max probability from start_node to node x
        edge_candidates = [] #e.g: [ [13, 0.7] ], a list of [node_num, max_prob_to_that_node]
        if start_node not in get_child:
            return 0
        for child in get_child[start_node]:
            get_max_prob[child] = get_succ_prob[self.get_pair(start_node, child)]
            edge_candidates.append([child, get_max_prob[child]])
        print("visited: ", visited)
        print(f"get_max_prob: ", get_max_prob)
        print("edge_candidates: ", edge_candidates)
        # edge_candidates =[ [B, 0.2], [C, 0.3], [D, 0.4] ]
        
        def find_next_node(end_node):
            if len(edge_candidates) == 0:
                self.max_probability = 0
                return 
            # find the next node 
            max_prob_to_node, next_node, index = -1, -1, -1
            for idx, edge_candidate in enumerate(edge_candidates):
                node, prob = edge_candidate
                if prob > max_prob_to_node:
                    max_prob_to_node = prob
                    next_node = node
                    index = idx
            print("next selected node: ", next_node, max_prob_to_node)
            if next_node == end_node:
                print("END TURN: ", max_prob_to_node)
                self.max_probability = max_prob_to_node
                return max_prob_to_node
            
            # add children nodes of selected node and their correspond max_prob_to_that_node
            # remove the selected node in the edge_candidates, add it to visited
            visited.add(next_node)
            del edge_candidates[index]
            
            print("remove selected node, edge_candidates: ", edge_candidates)
            for child in get_child[next_node]:
                if child not in visited:
                    _max_prob_to_node = get_max_prob[next_node] * get_succ_prob[self.get_pair(next_node, child)]
                    if child in get_max_prob:
                        if get_max_prob[child] < _max_prob_to_node:
                            get_max_prob[child] =  _max_prob_to_node
                            # update edge_candidates
                            for idx, edge in enumerate(edge_candidates):
                                _node, max_prob = edge
                                if _node == child:
                                    edge_candidates[idx][1] = _max_prob_to_node
                                    
                        else:
                            pass
                            
                    else:
                        get_max_prob[child] = _max_prob_to_node
                        edge_candidates.append([child, get_max_prob[child]])
                    print("selected child(s): ", [child, _max_prob_to_node])
            print("New edge_candidates: ", edge_candidates)
            find_next_node(end_node)
                    
        find_next_node(end_node)
        return self.max_probability
    
    
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


# n = 5
# edges = [  [2,3],[ 1,2], [3,4],[1,3], [1,4], [0,1], [2,4], [0,4], [0,2]]
# succProb = [0.06, 0.26,  0.49,  0.25,  0.2,  0.64,  0.23,  0.21,   0.77]
# start= 0
# end= 3
# print(s.maxProbability(n, edges, succProb, start, end))         


# n = 500
# edges = [[193,229],[133,212],[224,465]]
# succProb = [0.91,0.78,0.64]
# start = 4
# end = 364
# print(s.maxProbability(n, edges, succProb, start, end))         


n = 4
edges =   [[0,1] , [0,2], [0,4], [2, 1], [2, 4]]
succProb = [0.64,   0.77,  0.21,  0.91,   0.44]
start = 0
end = 3

print(s.maxProbability(n, edges, succProb, start, end))    