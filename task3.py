import heapq
from typing import Dict, List, Tuple, Any

"""
Task 3: Trees and Dijkstra's Algorithm
"""

def find_shortest_paths(graph: Dict[Any, List[Tuple[Any, float]]], source: Any) -> Dict[Any, float]:
    """
    Implements Dijkstra's algorithm using a binary heap (min-priority queue)
    to find the shortest paths from the source vertex to all other vertices
    in a weighted graph with non-negative edge weights.

    Parameters:
        graph (Dict): Adjacency list representation of the graph.
                      Each key is a vertex, and the value is a list of tuples (neighbor, weight).
        source (Any): The starting vertex.

    Returns:
        Dict: A dictionary mapping each vertex to its shortest distance from the source.

    Raises:
        KeyError: If the source vertex is not in the graph.
    """
    if source not in graph:
        raise KeyError(f"Source vertex '{source}' not found in the graph.")

    # Initialize all distances to infinity, except the source
    shortest_distances: Dict[Any, float] = {vertex: float('inf') for vertex in graph}
    shortest_distances[source] = 0

    # Min-priority queue to select vertex with smallest known distance
    min_heap: List[Tuple[float, Any]] = [(0, source)]

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        # If this distance is outdated, skip it
        if current_distance > shortest_distances[current_vertex]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_vertex]:
            new_distance = current_distance + weight

            # If a shorter path is found
            if new_distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = new_distance
                heapq.heappush(min_heap, (new_distance, neighbor))

    return shortest_distances


# Usage
if __name__ == "__main__":
    # Graph Example
    weighted_graph = {
        'S': [('A', 7), ('B', 2)],
        'A': [('S', 7), ('B', 3), ('C', 4)],
        'B': [('S', 2), ('A', 3), ('D', 5)],
        'C': [('A', 4), ('D', 1), ('E', 7)],
        'D': [('B', 5), ('C', 1), ('E', 2)],
        'E': [('C', 7), ('D', 2)]
    }

    # Define the source node for Dijkstra's algorithm
    # All shortest paths will be computed from this node
    source_node = 'S'

    try:
        shortest_paths = find_shortest_paths(weighted_graph, source_node)
        print(f"Shortest paths from '{source_node}':")
        for vertex, distance in shortest_paths.items():
            print(f"  to {vertex}: {distance}")
    except KeyError as e:
        print(f"Error: {e}")
