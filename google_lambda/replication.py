from fractions import gcd

# from http://stackoverflow.com/a/33409034
def calculate (x, y):
    if y == 0: return -1

    return calculate (y, x%y) + x/y

def answer(M, F):
    M, F=int(M), int(F)
    if gcd(M, F) != 1: return "impossible"

    return str(calculate(max(M, F), min(M, F)))