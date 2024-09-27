from dataclasses import dataclass
from pprint import pprint
from typing import Optional


@dataclass
class Node:
    value: int
    left: Optional[object] = None
    right: Optional[object] = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value, root=None):
        if root is None:
            root = self.root

        if not root:
            self.root = Node(value)
            return self

        if value > self.root.value:
            if self.root.right:
                self.insert(value, root)
            else:
                self.root.right = Node(value)
        elif value < self.root.value:
            if self.root.left:
                self.insert(value, root)
            else:
                self.root.left = Node(value)


if __name__ == "__main__":
    tree = BinaryTree()
    for i in [219, 498, 2, 34, 33, 665, 67, 345, 7, 8, 4]:
        tree.insert(i)
    pprint(tree.root)
