from heapq import heappop, heappush
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        ## Python’s `heapq` pops the smallest value first. Store **negative probabilities** so the path with the highest probability comes out first.


        for (u, v), edge_prob in zip(edges, succProb):
            graph[u].append((v, edge_prob))
            graph[v].append((u, edge_prob))
        prob = [0.0] * n
        prob[start_node] = 1.0
        heap = [(-1.0, start_node)]

        while heap:
            negative_prob, node = heappop(heap)
            curr_prob = -negative_prob

            if curr_prob < prob[node]:
                continue

            if node == end_node:
                return curr_prob

            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob

                if new_prob > prob[neighbor]:
                    prob[neighbor] = new_prob
                    heappush(heap, (-new_prob, neighbor))

        return 0.0