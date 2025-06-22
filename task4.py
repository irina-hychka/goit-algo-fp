import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Optional, Dict, Any, Tuple

"""
Task 4: Binary Heap Visualization
"""

class Node:
    """Class representing a node in a binary tree."""
    def __init__(self, key, color="skyblue"):
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph: nx.DiGraph, node: Optional[Node], pos: Dict[str, Tuple[float, float]], x: float = 0, y: float = 0, layer: int = 1) -> None:
    """
    Recursively adds nodes and edges to a networkx graph based on the binary tree structure.

    Args:
        graph: The directed graph to populate.
        node: The current node being processed.
        pos: A dictionary storing positions for each node (used in plotting).
        x, y: The position coordinates of the current node.
        layer: The current depth level in the tree.
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x - 1 / 2 ** layer
            pos[node.left.id] = (left_x, y - 1)
            add_edges(graph, node.left, pos, x=left_x, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_x = x + 1 / 2 ** layer
            pos[node.right.id] = (right_x, y - 1)
            add_edges(graph, node.right, pos, x=right_x, y=y - 1, layer=layer + 1)

def draw_tree(tree_root: Node) -> None:
    """
    Visualizes a binary tree using networkx and matplotlib.

    Args:
        tree_root: The root node of the tree to draw.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    node_colors = [data['color'] for _, data in tree.nodes(data=True)]
    node_labels = {node: data['label'] for node, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=node_labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.title("Binary Heap Tree Visualization")
    plt.show()

def build_heap_tree(heap_array: List[Any], i: int = 0) -> Optional[Node]:
    """
    Recursively builds a binary tree representation from a heap array.

    Args:
        heap_array: List representation of the heap.
        i: Current index in the array (default is 0, the root).

    Returns:
        The root node of the resulting binary tree.
    """
    if i < len(heap_array):
        node = Node(heap_array[i])
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        node.left = build_heap_tree(heap_array, left_index)
        node.right = build_heap_tree(heap_array, right_index)
        return node
    return None

# Usage
if __name__ == "__main__":
    print("Visualizing Binary Heap...")

    # Example:
    raw_values = [1, 3, 2, 7, 5, 4, 6, 15, 14, 13, 12, 11, 10, 9, 8]

    # Convert to min-heap
    heapq.heapify(raw_values)

    # Build binary tree from heap
    heap_tree = build_heap_tree(raw_values)

    # Draw the heap tree
    if heap_tree:
        draw_tree(heap_tree)
    else:
        print("Heap is empty. Nothing to visualize.")
