import heapq
import math


def dijsktra(graph, start):
    distances = {}
    for vertex in graph:
        distances[vertex] = math.inf

    distances[start] = 0

    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    visited = set()

    while len(priority_queue) > 0:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        neighbours = graph[current_vertex]

        for neighbour, weight in neighbours:
            distance = current_distance + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance

                heapq.heappush(priority_queue, (distance, neighbour))

    return distances
