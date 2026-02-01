class Node:
    LIMITS = {"ATOM": 0, "NOT": 1, "AND": 2, "OR": 2, "IMPLIES": 2}

    def __init__(self, data, node_type):
        self.data = data
        self.node_type = node_type
        self.children = []

    def add_child(self, child_node):
        max_allowed = self.LIMITS.get(self.node_type, 0)
        if len(self.children) >= max_allowed:
            raise ValueError(f"{self.node_type} exceeds limit of {max_allowed} children")
        self.children.append(child_node)

    def render(self):
        if self.node_type == "ATOM":
            return self.data

        if self.node_type == "NOT":
            child_str = self.children[0].render()
            return f"¬({child_str})"
        
        symbols = {"AND": "∧", "OR": "∨", "IMPLIES": "→"}

        if self.node_type in symbols:
            symbol = symbols[self.node_type]
            left = self.children[0].render()
            right = self.children[1].render()
            return f"({left} {symbol} {right})"

    def __repr__(self):
        return f"Node({self.node_type}: {self.data})"
