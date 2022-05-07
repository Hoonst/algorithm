n, m = map(int, input().split())
sets = [{nn} for nn in range(n+1)]

targets = [list(map(int, input().split())) for _ in range(m)]

for exp, a, b in targets:
    for s in sets:
        if a in s:
            one = s
        if b in s:
            two = s

    if not exp:
        if one != two:
            three = one.union(two)
            sets.remove(one)
            sets.remove(two)
            sets.append(three)
        # else:
        #     sets.remove(one)
        

    elif exp:
        if one == two:
            print('YES')
        else:
            print('NO')