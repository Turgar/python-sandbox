import copy
import numpy as np
from fractions import gcd, Fraction

# lcm for a list, from: http://stackoverflow.com/a/37238140
def multi_gcd(numbers):
    print numbers
    if len(numbers) > 2:
        return reduce(lambda x, y: gcd(*[x, y]), numbers)

def answer(m):
    terminal_states = []
    transit_states = []

    # first, determine the terminal state rows
    for i, r in enumerate(m):
        is_terminal=True
        for j in r: is_terminal = is_terminal and j==0
        if is_terminal: terminal_states.append(i)
        else: transit_states.append(i)

    # next, create r and q matricies
    r, q = [], []

    for n in transit_states:
        rrow, qrow = [0]*len(terminal_states), [0]*len(transit_states)
        total = sum(m[n])

        if total > 0:
            for i in xrange(len(terminal_states)): rrow[i] = ( m[transit_states[n]][terminal_states[i]] / float(total) )
            for i in xrange(len(transit_states)): qrow[i] = ( m[transit_states[n]][transit_states[i]] / float(total) )

            # for i in xrange(len(terminal_states)): rrow[i] = ( m[transit_states[n]][terminal_states[i]] )
            # for i in xrange(len(transit_states)): qrow[i] = ( m[transit_states[n]][transit_states[i]] )

        r.append(rrow)
        q.append(qrow)

    r = np.matrix(r)
    q = np.matrix(q)

    F = np.linalg.inv(np.identity(len(q)) - q)
    FR = np.dot(F, r)

    # print FR

    IN = FR[0] # initial state row

    print IN[np.nonzero(IN)][0].tolist()[0]

    for n in IN[np.nonzero(IN)][0].tolist()[0]:
        print Fraction.from_float(n).limit_denominator()

    print gcd(7, 14)

    # .nonzero().tolist()[0]
    print type(IN[np.nonzero(IN)][0].tolist()[0])
    print multi_gcd(IN[np.nonzero(IN)][0].tolist()[0])

answer(
    [
        [0, 1, 0, 0, 0, 1],  # s0, the initial state, goes to s1 and s5 with equal probability
        [4, 0, 0, 3, 2, 0],  # s1 can become s0, s3, or s4, but with different probabilities
        [0, 0, 0, 0, 0, 0],  # s2 is terminal, and unreachable (never observed in practice)
        [0, 0, 0, 0, 0, 0],  # s3 is terminal
        [0, 0, 0, 0, 0, 0],  # s4 is terminal
        [0, 0, 0, 0, 0, 0],  # s5 is terminal
    ]
)