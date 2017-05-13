# search for the parent node value of the given value
def search(height, value):
    root = 2 ** height - 1
    if value >= root: return -1  # value is larger than tree

    while height > 1:
        # check left
        left = root - 2 ** (height - 1)
        if value == left: return root
        if value < left:
            height-=1
            root = left
            continue

        # check right
        right = root - 1
        if value == right: return root
        if value < right:
            height-=1
            root = right
            continue

        return -1

def answer(h, q):
    return [ search(h, i) for i in q ]

if __name__ == '__main__':
    print answer(3, [7, 3, 5, 1])
    # print answer(5, [19, 14, 28])