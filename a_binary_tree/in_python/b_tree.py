from dataclasses import dataclass


class Node:
    def __init__(self):
        self.keys: list[int] = list()
        self.children: list["Node"] = list()

    def sort_keys(self):
        center = self.keys[(len(self.keys) % 2) + 1]
        center.left_branch = [k for k in self.keys if k.value < center]
        center.right_branch = [k for k in self.keys if k.value > center]
        self.keys = center


class Tree:
    def __init__(self):
        self.max_keys = 4
        self.root = None
        self.nodes = list()

    def search(self, token, branch=None):
        for node in self.nodes:
            for key in node.keys:
                if token == key.value:
                    return True, token, node
                if token < key.value and key.left_branch:
                    branch = key.left_branch
                    self.search(token, branch)
                elif token > key.value and key.right_branch:
                    branch = key.right_branch
                    self.search(token, branch)
        return False, token, branch

    def insert(self, value):
        result, token, node = self.search(value)
        if result:
            return  # Duplicate value

        new_key = Key(value)
        node.keys.append(new_key)
        node.keys = sorted(node.keys, key=lambda k: k.value)
        if len(node.keys) > self.max_keys:
            # Split the keys up into new nodes.
            # The minimum allowable number is self.max_keys // 2
            node.sort_keys()

    def delete(self, value):
        result, token, branch = self.search(value):
        if result:
            branch.keys.remove()

