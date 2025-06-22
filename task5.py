import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from typing import List, Optional, Dict, Any, Tuple

"""
Task 5: Binary Tree Traversal Visualization
"""

class Node:
    """Class representing a node in a binary tree."""
    def __init__(self, key, color="#D3D3D3"):  # light gray default
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Unique ID for drawing

def add_edges(
    graph: nx.DiGraph,
    node: Optional[Node],
    pos: Dict[str, Tuple[float, float]],
    x: float = 0,
    y: float = 0,
    layer: int = 1
) -> None:
    """
    Recursively adds nodes and edges to the graph
    and positions them in a tree layout.
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

def draw_tree(tree_root: Node, title: str = "") -> None:
    """
    Draws a binary tree using NetworkX and matplotlib.

    Args:
        tree_root: Root of the binary tree.
        title: Title of the visualization.
    """
    plt.clf()
    plt.gcf().set_size_inches(12, 7)
    plt.title(title)

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    node_colors = [data['color'] for _, data in tree.nodes(data=True)]
    node_labels = {node: data['label'] for node, data in tree.nodes(data=True)}

    nx.draw(
        tree, pos=pos, labels=node_labels, arrows=False,
        node_size=2500, node_color=node_colors
    )
    plt.show()

def build_heap_tree(heap_array: List[Any], i: int = 0) -> Optional[Node]:
    """
    Builds a binary tree from a heap array recursively.

    Args:
        heap_array: List representing the heap.
        i: Current index in the array.

    Returns:
        Root node of the binary tree.
    """
    if i < len(heap_array):
        node = Node(heap_array[i])
        node.left = build_heap_tree(heap_array, 2 * i + 1)
        node.right = build_heap_tree(heap_array, 2 * i + 2)
        return node
    return None

def generate_gradient(n: int) -> List[str]:
    """
    Generates a gradient of n colors from dark blue to light blue.

    Args:
        n: Number of colors.

    Returns:
        List of hex color strings.
    """
    colors = []
    for i in range(n):
        r = int((0   * (n - 1 - i) + 173 * i) / (n - 1))
        g = int((0   * (n - 1 - i) + 216 * i) / (n - 1))
        b = int((139 * (n - 1 - i) + 230 * i) / (n - 1))
        colors.append(f'#{r:02x}{g:02x}{b:02x}')
    return colors

def bfs_traversal(root: Node) -> List[Node]:
    """
    Performs breadth-first traversal using a queue.

    Args:
        root: Root of the tree.

    Returns:
        List of visited nodes in BFS order.
    """
    if not root:
        return []
    visited = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        visited.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited

def dfs_traversal(root: Node) -> List[Node]:
    """
    Performs depth-first traversal using a stack.

    Args:
        root: Root of the tree.

    Returns:
        List of visited nodes in DFS order.
    """
    if not root:
        return []
    visited = []
    stack = [root]
    while stack:
        node = stack.pop()
        visited.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited

def apply_traversal_and_color(root: Node, traversal_func, title: str):
    """
    Applies a traversal to the tree and updates node colors
    according to traversal order using a blue gradient.

    Args:
        root: Root of the binary tree.
        traversal_func: Traversal function (bfs or dfs).
        title: Plot title.
    """
    visited = traversal_func(root)
    gradient = generate_gradient(len(visited))
    for node, color in zip(visited, gradient):
        node.color = color
    draw_tree(root, title=title)

# Usage
if __name__ == "__main__":
    print("Binary Heap BFS and DFS Traversal Visualization...")

    # Array of values to build a balanced heap
    raw_values = [1, 3, 2, 7, 5, 4, 6, 15, 14, 13, 12, 11, 10, 9, 8]
    heapq.heapify(raw_values)  # Convert to min-heap

    # Build binary tree from heap
    tree_root = build_heap_tree(raw_values)

    if tree_root:
        # BFS visualization
        apply_traversal_and_color(tree_root, bfs_traversal, "Breadth-First Traversal Visualization")

        # Rebuild tree for DFS (to reset colors)
        tree_root = build_heap_tree(raw_values)

        # DFS visualization
        apply_traversal_and_color(tree_root, dfs_traversal, "Depth-First Traversal Visualization")
    else:
        print("Tree is empty.")
