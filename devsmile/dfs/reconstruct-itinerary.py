class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        airline_list = collections.defaultdict(list)

        for key, value in sorted(tickets):
            airline_list[key].append(value)

        path = []

        def dfs(a):
            while airline_list[a]:
                dfs(airline_list[a].pop(0))
            path.append(a)

        dfs("JFK")
        return path[::-1]
