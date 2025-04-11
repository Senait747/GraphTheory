class DFS:
    def __init__(self, graph):
        self.graph = graph

    def run(self):
        result = []
        visited = set()
        stack = []

        start_node = self.graph.get_nodes()[0]
        stack.append(start_node)
        visited.add(start_node)

        while stack:
            current_node = stack.pop()
            node_edge_map = {}

            for edge in self.graph.get_edges():
                if edge.start == current_node and edge.end not in visited:
                    stack.append(edge.end)
                    visited.add(edge.end)
                    node_edge_map[current_node] = edge

            if node_edge_map:
                result.append(node_edge_map)

        return result