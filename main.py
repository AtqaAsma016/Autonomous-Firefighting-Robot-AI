import heapq

graph = {
    'S': [('A', 3), ('B', 6)],
    'A': [('W', 4), ('C', 8)],
    'B': [('W', 3), ('G', 9)],
    'W': [('C', 2), ('G', 10)],
    'C': [('G', 5)],
    'G': []
}

h_to_W = {'S':7,'A':4,'B':3,'C':3,'W':0,'G':0}
h_to_G = {'S':10,'A':9,'B':9,'C':5,'W':10,'G':0}

def heuristic(node, has_water):
    if not has_water:
        return h_to_W[node] + h_to_G['W']
    return h_to_G[node]

def a_star():
    START = 'S'
    ARMOR_MAX = 24     
    COLLAPSE_TIME = 10 
    IS_EVEN = True     

    pq = []
    heapq.heappush(pq, (0, START, ARMOR_MAX, 0, False, False, [START]))

    visited = set()
    nodes_expanded = 0

    while pq:
        f, node, armor, time, has_water, repaired, path = heapq.heappop(pq)

        state_id = (node, has_water, repaired)
        if state_id in visited:
            continue
        visited.add(state_id)

        nodes_expanded += 1

        if node == 'G' and has_water:
            print("Final Path:", " → ".join(path))
            print("Total Time:", time)
            print("Remaining Armor:", armor)
            print("Nodes Expanded:", nodes_expanded)
            return

        for neighbor, cost in graph[node]:
            new_time = time + cost
            new_armor = armor - cost

            if new_armor <= 0:
                continue

            if IS_EVEN and node == 'B' and neighbor == 'G' and new_time >= COLLAPSE_TIME:
                continue

            new_has_water = has_water
            new_repaired = repaired

            if neighbor == 'W':
                new_has_water = True

            if neighbor == 'B' and not repaired:
                new_armor = ARMOR_MAX
                new_repaired = True

            new_f = new_time + heuristic(neighbor, new_has_water)

            heapq.heappush(pq, (
                new_f,
                neighbor,
                new_armor,
                new_time,
                new_has_water,
                new_repaired,
                path + [neighbor]
            ))

    print("No Solution Found")

a_star()
