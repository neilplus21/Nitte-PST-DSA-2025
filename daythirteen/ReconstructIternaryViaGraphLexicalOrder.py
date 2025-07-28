from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        # Build graph with min-heaps for lexical order
        for src, dst in tickets: heapq.heappush(graph[src], dst)
        itinerary = []
        def dfs(airport):
            while graph[airport]:
                next_stop = heapq.heappop(graph[airport])
                dfs(next_stop)
            itinerary.append(airport)  # Post-order insert
        dfs("JFK")
        return itinerary[::-1]  # Reverse to get correct order
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],
           ["ATL","JFK"],["ATL","SFO"]]
sol = Solution()
print(sol.findItinerary(tickets))
# Output: ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
print(sol.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))