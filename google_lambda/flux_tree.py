class FluxNode:
    def __init__(self, value=None):
        self.left=None
        self.right=None
        self.value=value

    def __repr__(self):
        return '[Node {0}]'.format(self.value)

class FluxTree:
    def __init__(self, height=1):
        self.root = FluxNode()
        self.height = height
        self.build()
        self.label()

    # build this flux tree with height h
    def build(self):
        FluxTree.add_level(self.root, self.height)

    @staticmethod
    def add_level(parent, h):
        if h <= 1: return

        parent.left = FluxNode()
        parent.right = FluxNode()

        FluxTree.add_level(parent.left, h - 1)
        FluxTree.add_level(parent.right, h - 1)

    # postorder traversal, label entire tree
    def label(self):
        FluxTree.label_search(self.root, 1)

    @staticmethod
    def label_search(node, value):
        if node.left is not None: value = FluxTree.label_search(node.left, value)
        if node.right is not None: value = FluxTree.label_search(node.right, value)

        node.value=value
        return value+1

    # search for the parent node value of the given value
    def search(self, value):
        if value >= 2**self.height-1: return -1 # value is larger than tree

        return FluxTree.parent_search(self.root, value)

    @staticmethod
    def parent_search(node, value):
        if node.left is not None:
            if node.left.value == value: return node.value
            if value < node.left.value: return FluxTree.parent_search(node.left, value)

        if node.right is not None:
            if node.right.value == value: return node.value
            else: return FluxTree.parent_search(node.right, value)

        return None

    # def out(self):
    #     print ' '.join(FluxTree.print_search(self.root))
    #
    # @staticmethod
    # def print_search(node):
    #     ret=[]
    #     if node.left is not None: ret += FluxTree.print_search(node.left)
    #     if node.right is not None: ret += FluxTree.print_search(node.right)
    #
    #     ret.append(str(node.value))
    #     return ret

    def out(self):
        # print '\n'.join(FluxTree.print_search(self.root))
        print "Leaves: " + ' '.join(FluxTree.leaf_search(self.root))
        print "Parents: " + ' '.join(FluxTree.parents_search(self.root))

    @staticmethod
    def print_search(node):
        ret=[' '.join([str(node), str(node.left), str(node.right)])]
        ret = []

        if node.left is not None: ret += FluxTree.print_search(node.left)
        if node.right is not None: ret += FluxTree.print_search(node.right)

        if node.right is not None: print node.right.value == (node.value - 1)

        return ret

    @staticmethod
    def leaf_search(node):
        if node.left is None: return [ str(node.value) ]
        else: return FluxTree.leaf_search(node.left) + FluxTree.leaf_search(node.right)

    @staticmethod
    def parents_search(node):
        if node.left is not None: return FluxTree.parents_search(node.left) + FluxTree.parents_search(node.right) + [str(node.value)]
        else: return []

def answer(h, q):
    tree = FluxTree(height=h)
    tree.out()

    return [ tree.search(i) for i in q ]

if __name__ == '__main__':
    # print answer(3, [7, 3, 5, 1])
    # print answer(5, [19, 14, 28])
    print answer(5, [19, 14, 28])