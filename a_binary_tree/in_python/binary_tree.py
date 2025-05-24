from dataclasses import dataclass
from pprint import pprint
import random
from typing import Optional


@dataclass
class Node:
    value: int
    left: Optional[object] = None
    right: Optional[object] = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value > node.value:
            if node.right:
                self._insert(value, node.right)
            else:
                node.right = Node(value)
        elif value < node.value:
            if node.left:
                self._insert(value, node.left)
            else:
                node.left = Node(value)

    def traverse_in_order(self, node=None):
        if node:
            self.traverse_in_order(node.left)
            print(node.left.value)
            self.traverse_in_order(node.right)


if __name__ == "__main__":
    tree = BinaryTree()
    for i in [random.choice(range(1000)) for _ in range(20)]:
        tree.insert(i)
    pprint(tree.root)
    print(tree.traverse_in_order(tree.root))
