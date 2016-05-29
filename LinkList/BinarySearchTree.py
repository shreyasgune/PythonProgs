class Node:
    def __init__(self,val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root,node):
    y = None
    x = root
    z = node

    while x is not None:
        y = x
        if z.data < x.data:
            x = x.l_child
        else:
            x = x.r_child

    z.parent = y
    if y ==None:
        root = z
    elif z.data<y.data:
        y.l_child=z
    else:
        y.r_child=z




def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print(root.data)
    in_order_print(root.r_child)

r = Node(3)
binary_insert(r,Node(7))
binary_insert(r,Node(1))
binary_insert(r,Node(5))

in_order_print(r)
