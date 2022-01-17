N = int(input())
def flooring(n):
    accum = 1
    m = 1
    while n > accum:
        accum += (6*m)
        # wrong answer (m+1) * (m+2)
        m += 1
    return m
print(flooring(N))