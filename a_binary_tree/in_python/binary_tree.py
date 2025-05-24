from dataclasses import dataclass
from pprint import pprint
from typing import Optional


@dataclass
class Node:
    value: int
    left: Optional[object] = None
    right: Optional[object] = None


def figure_out_b_tree(values: list[int]):
    """Every tree consists of nodes.
    The nodes contain left, right pointers and a value,
    so each node is a mini-b-tree. Therefore we need to start with a node.
    """
    print("Running B Tree Thingy...\n\n")
    tree = Node(12)

    def determine_where_the_node_goes(new_value, parent=tree):
        """So I think there's an aspect of left < root < right"""
        if new_value > parent.value:
            # look right
            if parent.right:
                determine_where_the_node_goes(new_value, parent.right)
            else:
                parent.right = Node(new_value)
        elif new_value < parent.value:
            # look left
            if parent.left:
                determine_where_the_node_goes(new_value, parent.left)
            else:
                parent.left = Node(new_value)

    for i in values:
        determine_where_the_node_goes(i)

    return tree


if __name__ == "__main__":
    pprint(figure_out_b_tree([48, 22, 190, 4, 16, 7]))
