from collections import deque

# BFS Algorithm
class BFS:
    def __init__(self, graph):
        self.graph = graph

    def run(self):
        result = []
        visited = set()
        queue = deque()

        start_node = self.graph.get_nodes()[0]  # Assuming the first node in the list is the starting point
        queue.append(start_node)
        visited.add(start_node)

        while queue:
            current_node = queue.popleft()
            node_edge_map = {}

            for edge in self.graph.get_edges():
                if edge.start == current_node and edge.end not in visited:
                    queue.append(edge.end)
                    visited.add(edge.end)
                    node_edge_map[current_node] = edge

            if node_edge_map:
                result.append(node_edge_map)

        return result

