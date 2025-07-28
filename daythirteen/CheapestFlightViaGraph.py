import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, flights, src, dst, k):
        graph = defaultdict(list)
        for origin, dest, cost in flights: graph[origin].append((dest, cost))
        # Priority queue: (price, city, stops)
        heap = [(0, src, 0)]
        while heap:
            price, city, stops = heapq.heappop(heap)
            if city == dst: return price
            if stops <= k:
                for nei, p in graph[city]: heapq.heappush(heap, (price + p, nei, stops + 1))
        return -1
print(Solution().findCheapestPrice(
    [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
    )  # Output: 700
print(Solution().findCheapestPrice(
     [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
    )  # Output: 200
print(Solution().findCheapestPrice(
    [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)
    )  # Output: 500

# from collections import deque,defaultdict
# def cheap_path_with_k_stops(edges,src,destination,max_stops):

#     adjacency_list = defaultdict(list)
#     weight_list = {}
#     for source,dest,cost in edges:
#         adjacency_list[source].append(dest)
#         weight_list[(source,dest)] = cost
#         weight_list[(dest,source)] = cost
        
#     queue = deque()
#     queue.append((0,src,0))
#     min_cost = defaultdict(lambda :float("inf"))
#     min_cost[src] = 0
    
#     while queue:
#         cost ,node,stops = queue.popleft()
        
#         if stops>max_stops:
#             continue
        
#         for neighbour in adjacency_list[node]:
#             travel_cost  = weight_list[(node,neighbour)]+cost
#             if travel_cost<min_cost[neighbour]:
#                 min_cost[neighbour] = travel_cost
#                 queue.append((travel_cost,neighbour,stops+1))

#     return -1 if destination not in min_cost else min_cost[destination]
    
# print(cheap_path_with_k_stops(
#     [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
#     )  # Output: 700
# print(cheap_path_with_k_stops(
#      [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
#     )  # Output: 200
# print(cheap_path_with_k_stops(
#     [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)
#     )  # Output: 500