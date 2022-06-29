# author: Melanie Burns
# Due: June 28, 2022
# email: burns.me@northeasturn.edu
# StudentID: 002923383
# Base code given in assignment 4, but everything else is my own

# An AVL tree is a binary search tree such that, for each node x, the height of the left and
# right subtrees of x differ by at most 1.

class Node:
    def __init__(self, key: int, p=None, l=None, r=None, h=1):
        self.left = l
        self.right = r
        self.parent = p
        self.value = key
        self.height = h


class Tree:
    def __init__(self, key):
        self.root = Node(key)

    def print(self, space=0):
        self._print_node(self.root, space)

    def _print_node(self, node: Node, space: int):
        space += 10
        if node:
            self._print_node(node.left, space)
            for i in range(10, space):
                print(end=" ")
            print("Val: " + str(node.value) + " H: " + str(node.height))
            self._print_node(node.right, space)


def left_rotate(T: Tree, x: Node):
    y = x.right
    x.right = y.left

    if y.left:
        y.left.parent = x

    y.parent = x.parent

    if not x.parent:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.left = x
    x.parent = y

    # update height
    update_height(x)
    update_height(y)


def right_rotate(T: Tree, y: Node):
    x = y.left
    y.left = x.right

    if x.right:
        x.right.parent = y
    x.parent = y.parent
    if not y.parent:
        T.root = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    x.right = y
    y.parent = x

    # update height


def avl_insert(T, key):
    y, x = None, T.root
    while x:
        y = x
        if key == x.value:
            print("The given key already exists:", key)
            return
        elif key < x.value:
            x = x.left
        else:
            x = x.right

    z = Node(key, y)
    if not y:
        T.root = z
    elif key < y.value:
        y.left = z
    else:
        y.right = z
    avl_insert_fixup(T, z)


### Start of my code ###
def balance_factor(z: Node):
    left, right = 0, 0
    if z.left:
        left = z.left.height

    if z.right:
        right = z.right.height

    return left - right


def update_height(z: Node):
    left, right = 0, 0
    if z.left:
        left = z.left.height

    if z.right:
        right = z.right.height

    z.height = 1 + max(left, right)


def avl_insert_fixup(T: Tree, z: Node):
    # Maybe I should calculate the height by doing postive negative
    # 0 meaning both sides are even. - if weighted to left and postive if weighted to right?
    # 1. calculate the height
    update_height(z.parent)

    x = z
    while x:
        balance = balance_factor(x)
        print(balance)

        # left subtree
        if balance > 1:
            sub_balance = balance_factor(x.left)
            # I noticed this pattern when doing it by hand, I think it's right for all cases.
            if sub_balance < 0:
                left_rotate(T, x.left)
            right_rotate(T, x)
            print("\t" + str(balance_factor(x)))
        # right subtree
        elif balance < -1:
            sub_balance = balance_factor(x.right)
            if sub_balance > 0:
                right_rotate(T, x.right)
            left_rotate(T, x)
            print("\t" + str(balance_factor(x)))

        x = x.parent


# Sorry I know I normally set up nice pytests, but this one I manualy tested. I did walk through different ones
# but the only below is the testing left right rotation

## test this avl
t = Tree(50)
avl_insert(t, 30)
t.print()
print()
avl_insert(t, 40)

t.print()
