graph = [list(range(3)) for _ in range(3)]
print(graph)

def rotate90(graph_):
    return [list(i for i in zip(*graph_)]

def rotate90_list(graph_):
    return [list(reversed(i)) for i in graph]
print(rotate90(graph))
print(rotate90_list(graph))

print(list(zip(*graph)))