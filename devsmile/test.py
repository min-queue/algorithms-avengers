import heapq as hq


# recipes = ['A 3', 'B 2']
# n = 2
# orders = ['A 1', 'A 2', 'B 3', 'B 4']

recipes = ["P 8", "F 2", "S 3"]
n = 3
orders = ["P 1", "F 2", "S 4", "S 6", "P 7", "S 8"]


def solution(recipes, n, orders):
    my_recipes = dict()
    places = n * [1]
    hq.heapify(places)
    last_idx = len(orders) - 1
    print(places)
    for r in recipes:
        my_recipes[r.split()[0]] = int(r.split()[1])

    for idx, o in enumerate(orders):
        menu = o.split()[0]
        menu_time = int(o.split()[1])
        place_time = hq.heappop(places)
        time = 0
        if place_time >= menu_time:
            place_time += my_recipes[menu]
            time = place_time
        else:
            menu_time += my_recipes[menu]
            time = menu_time
        if idx == last_idx:
            return time
        else:
            hq.heappush(places, time)
        # print(places)
    # print(my_recipes)


print(solution(recipes, n, orders))
