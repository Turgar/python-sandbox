import math

def answer(src, dest):
    dx=abs((src//8)-(dest//8))
    dy=abs((src%8)-(dest%8))

    # exception cases
    if dx == dy and dx == 2: return 4  # diagonal by 2 case
    if dx + dy == 1: return 3 # adjacent case
    if src in [0, 7, 56, 63] and dx==dy==1: return 4 # corner

    # from https://math.stackexchange.com/a/1137144
    mp=math.ceil(max([ dx/2.0, dy/2.0, (dx+dy)/3.0 ]))

    return int(mp + (mp + dx + dy)%2)

for i in xrange(0, 64):
    print '({0}, {1}): {2}'.format(i//8, i%8, answer(0, i))