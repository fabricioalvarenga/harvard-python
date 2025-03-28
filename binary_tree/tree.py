from __future__ import annotations

class Node:
    ID_COUNTER: int = 0

    def __init__(self, name: str, value: int, is_root: bool = False):
        Node.ID_COUNTER += 1

        self.name: str = name
        self.value: int = value                        
        self.id: int = Node.ID_COUNTER
        self.is_root: bool = is_root                  
        self.ascending: Node | None = None
        self.descendants: list[Node] = []

    def __str__(self) -> str:
        return f"({self.id}, {self.name}, {self.value})"


class Tree:
    def __init__(self, nodes: list[Node]):
        self.nodes: list[Node] = []
        self.count: int = 0
        self.add_nodes(nodes)

    def __str__(self) -> str:
        s: str = "" 
        for node in self.nodes:
            s += f"ID: {node.id}, Name: {node.name}, Value: {node.value}, Ascending: {node.ascending}, Descendants: {node.descendants}\n"

        return s

    def add_node(self, node: Node):
        # No two nodes with the same name are allowed in the tree
        if self.get_node_by_name(node.name):
            return
        self.nodes.append(node)
        self.count += 1

    def add_nodes(self, nodes: list[Node]):
        for node in nodes:
            self.add_node(node)

    def get_root_node(self) -> Node | None:
        for node in self.nodes:
            if node.is_root:
                return node

        return None

    def get_node_by_name(self, name: str) -> Node | None:
        return next((node for node in self.nodes if node.name == name), None)

    def set_descendant(self, ascending: Node, descendant: Node):
        ascending.descendants.append(descendant)
        descendant.ascending = ascending

    def set_descendants(self, pair_of_nodes: list[dict[str, Node]]):
        for pair in pair_of_nodes:
            self.set_descendant(pair["ascending"], pair["descendant"])

    def walk_through(self, node: Node | None):
        if not node:
            return

        print(node)

        for n in node.descendants:
            self.walk_through(n)


def main():
    root_node: Node = Node("ROOT", 15, is_root = True)
    node2: Node = Node("N2", 8)
    node3: Node = Node("N3", 16)
    node4: Node = Node("N4", 6)
    node5: Node = Node("N5", 2)
    node6: Node = Node("N6", 3)
    node7: Node = Node("N7", 12)
    node8: Node = Node("N8", 23)
    node9: Node = Node("N9", 3)
    node10: Node = Node("N10", 42)
    node11: Node = Node("N11", 6)
    node12: Node = Node("N12", 35)
    node13: Node = Node("N13", 26)
    node15: Node = Node("N15", 51)
    node16: Node = Node("N16", 8)

    nodes: list[Node] = [
            root_node, node2, node3, node4, node5, node6,
            node7, node8, node9, node10, node11, node12,
            node13, node15, node16
    ]

    tree: Tree = Tree(nodes)

    tree.set_descendants([
        {"ascending": root_node, "descendant": node2},
        {"ascending": root_node, "descendant": node3},
        {"ascending": node2, "descendant": node4},
        {"ascending": node3, "descendant": node5},
        {"ascending": node3, "descendant": node6},
        {"ascending": node4, "descendant": node7},
        {"ascending": node4, "descendant": node8},
        {"ascending": node5, "descendant": node9},
        {"ascending": node6, "descendant": node10},
        {"ascending": node7, "descendant": node11},
        {"ascending": node8, "descendant": node12},
        {"ascending": node9, "descendant": node13},
        {"ascending": node10, "descendant": node15},
        {"ascending": node10, "descendant": node16}
    ])

    tree.walk_through(tree.get_root_node())


if __name__ == "__main__":
    main()
