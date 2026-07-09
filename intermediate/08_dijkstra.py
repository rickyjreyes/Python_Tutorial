# 08_dijkstra.py
#
# Dijkstra's algorithm finds the shortest path from one starting node
# to every other reachable node in a weighted graph.

import heapq


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    previous = {node: None for node in graph}
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (new_distance, neighbor))

    return distances, previous


def build_path(previous, target):
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path


graph = {
    "A": {"B": 4, "C": 2},
    "B": {"C": 1, "D": 5},
    "C": {"B": 1, "D": 8, "E": 10},
    "D": {"E": 2},
    "E": {},
}

distances, previous = dijkstra(graph, "A")

print("Shortest distances from A:", distances)
print("Shortest path to E:", build_path(previous, "E"))
