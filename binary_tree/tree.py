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

    def add_descendant(self, node: Node):
        self.descendants.append(node)
        node.ascending = self


class Tree:
    def __init__(self, nodes: list[Node]):
        self.nodes: list[Node] = nodes
        self.count: int = len(nodes)

    def __str__(self) -> str:
        s: str = "" 
        for node in self.nodes:
            s += f"ID: {node.id}, Name: {node.name}, Value: {node.value}, Ascending: {node.ascending}, Descendants: {node.descendants}\n"
        return s

    def search_root(self) -> Node | None:
        for node in self.nodes:
            if node.is_root: return node

        return None

    def walk_through(self, n: Node | None):
        if not n: return

        print(n)
        for node in n.descendants:
            self.walk_through(node)


def main():
    root_node: Node = Node("N1", 15, is_root = True)
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
 
    root_node.add_descendant(node2)
    root_node.add_descendant(node3)

    node2.add_descendant(node4)
    
    node3.add_descendant(node5)
    node3.add_descendant(node6)

    node4.add_descendant(node7)
    node4.add_descendant(node8)

    node5.add_descendant(node9)

    node6.add_descendant(node10)

    node7.add_descendant(node11)

    node8.add_descendant(node12)

    node9.add_descendant(node13)

    node10.add_descendant(node15)
    node10.add_descendant(node16)

    nodes: list[Node] = [
            root_node, node2, node3, node4, node5, node6,
            node7, node8, node9, node10, node11, node12,
            node13, node15, node16
    ]

    tree: Tree = Tree(nodes)

    tree.walk_through(tree.search_root())


if __name__ == "__main__":
    main()
