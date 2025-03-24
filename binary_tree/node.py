from __future__ import annotations

class Node:
    ID_COUNTER: int = 0

    def __init__(self, value: int, is_root: bool = False):
        Node.ID_COUNTER += 1

        self._id: int = Node.ID_COUNTER                # Propriedade privada à classe e suas subclasses
        self.value: int = value                        # Propriedade exposta
        self._is_root: bool = is_root                  # Propriedade privada à classe e suas subclasses
        self.__descending_nodes: list[Child_Node] = [] # Propriedade privada apenas à classe, evitando que os descendentes sejam setados por qualquer nó

    @property
    def id(self) -> int: return self._id # Expõe o getter para fora da classe

    @property
    def is_root(self) -> bool: return self._is_root # Expõe o getter para fora da classe

    def _add_descendant(self, node: Child_Node): # Método privado para a classe e suas subclasses
        self.__descending_nodes.append(node)

    def get_descendants(self) -> list[Child_Node]: return self.__descending_nodes # Método exposto, permitindo que se consulte os descendentes de um nó


class Root_Node(Node):
    def __init__(self, value: int):
        super().__init__(value, is_root = True)

    def add_descendant(self, node: Child_Node):
        super()._add_descendant(node)


class Child_Node(Node):
    def __init__(self, value: int, ascending_node: Root_Node | Child_Node):
        super().__init__(value)
        self._ascending_node: Root_Node | Child_Node = ascending_node
        self._ascending_node._add_descendant(self)

    @property
    def ascending_node(self) -> Root_Node | Child_Node: return self._ascending_node


def main():
    root_node: Root_Node = Root_Node(10)
    child_node1: Child_Node = Child_Node(20, root_node)
    child_node2: Child_Node = Child_Node(30, root_node)
    child_node3: Child_Node = Child_Node(40, child_node2)

    root_node.add_descendant(child_node1)
    root_node.add_descendant(child_node2)

    print(f"Root  Node   => ID: {root_node.id}, Value: {root_node.value}, Descending: {root_node.get_descendants()[0].id}")
    print(f"Child Node 1 => ID: {child_node1.id}, Value: {child_node1.value}, Ascending: {child_node1.ascending_node.id}")
    print(f"Child Node 2 => ID: {child_node2.id}, Value: {child_node2.value}, Ascending: {child_node2.ascending_node.id}, Descending: {child_node2.get_descendants()[0].id}")
    print(f"Child Node 3 => ID: {child_node3.id}, Value: {child_node3.value}, Ascending: {child_node3.ascending_node.id}")


if __name__ == "__main__":
    main()
