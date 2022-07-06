# author: Melanie Burns
# Due: June 21, 2022
# email: burns.me@northeasturn.edu
# StudentID: 002923383
# Base code given in assignment 4, but everything else is my own

import pytest

class MinHeap:
    def __init__(self, arrays: list[list[int]]):
        self.heap = []
        for item in arrays:
            self.add(item)

    def heapify(self, root: int = 0):
        if not self.heap:
            return None

        smallest_node = root
        l_child = 2*root + 1
        r_child = 2*root + 2

        if l_child < len(self.heap) and self.heap[l_child] < self.heap[smallest_node]:
            smallest_node = l_child

        if r_child < len(self.heap) and self.heap[r_child] < self.heap[smallest_node]:
            smallest_node = r_child

        if smallest_node != root:
            self.heap[root], self.heap[smallest_node] = self.heap[smallest_node], self.heap[root]
            self.heapify(root)

    def add(self, array: list[int]):
        self.heap.append(array)
        self.heapify()

    def get_min(self):
        if not self.heap:
            return None

        smallest = self.heap[0].pop(0)

        if len(self.heap[0]) == 0:
            if len(self.heap) > 1:
                self.heap[0] = self.heap.pop()
            else:
                self.heap = []
        self.heapify()
        return smallest


def find_k_smallest_using_heap(input_arrays, k):
    # create a min heap out of the input arrays
    min_heap = MinHeap(input_arrays)
    min = None

    # for k times remove the smallest
    for i in range(k):
        min = min_heap.get_min()

    # return none if k goes outside n
    return min


class Node:
    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.value = key


def k_small(root: Node, k, counter):
    # we have tried to go past a leaf, go back up to the leaf
    if root is None:
        return root, counter

    l_child, counter = k_small(root.left, k, counter)

    if l_child is None:
        # we're at the k_smallest
        counter += 1
        if counter == k:
            return root, counter  # this will carry the smallest node and the counter up the stack
    else:
        return l_child, counter # we know it's down that route

    # if we didn't find and left is exhausted go to the right
    r_child, counter = k_small(root.right, k, counter)
    return r_child, counter


def find_k_smallest_using_bst(root: Node, k):
    smallest_node, _ = k_small(root, k, counter=0)
    return smallest_node.value


@pytest.mark.parametrize("arrays,k,expected", [
    ([[2, 3, 3, 4], [1, 5], [1, 2, 4]], 4, 2),  # given
    ([[2, 3, 3, 4], [1, 5], [1, 2, 4]], 7, 4),
    ([[2, 3, 3, 4], [1, 5], [1, 2, 4]], 9, 5),
])
def test_find_k_smallest_using_heap(arrays, k, expected):
    assert find_k_smallest_using_heap(arrays, k) == expected


def build_example_bst():
    root = Node(41)
    root.left = Node(20)
    root.left.left = Node(11)
    root.left.right = Node(29)
    root.left.right.right = Node(32)

    root.right = Node(65)
    root.right.left = Node(50)
    root.right.right = Node(91)
    root.right.right.left = Node(72)
    root.right.right.right = Node(99)
    return root


@pytest.mark.parametrize("k,expected", [
    (4, 32),  # given
    (1, 11),  # given
    (6, 50),  # given
])
def test_find_k_smallest_using_bst(k, expected):
    root = build_example_bst()
    assert find_k_smallest_using_bst(root, k) == expected


if __name__ == '__main__':
    pytest.main()
