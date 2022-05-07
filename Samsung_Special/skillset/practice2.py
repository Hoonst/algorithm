target_size = 4
target = list(range(target_size))
answer = []
wanted_size = 3

def comb(idx, temp):
    if len(temp) == wanted_size:
        answer.append(temp)
        return
    
    for i in range(idx, target_size):
        comb(i+1, temp + [target[i]])

comb(0, [])

for ans in answer:
    print(ans)

target_size = 4
target = list(range(target_size))
answer = []
wanted_size = 3
visited = [0 for _ in range(target_size)]

def perm(temp):
    if len(temp) == wanted_size:
        answer.append(temp[:])
        return

    for i, val in enumerate(target):
        if visited[i]:
            continue
            
        temp.append(val)
        visited[i] = 1

        perm(temp)

        temp.pop()
        visited[i] = 0
    
perm([])
for ans in answer:
    print(ans)