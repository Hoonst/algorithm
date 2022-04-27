def graph_rotation(graph_):
    return [list(reversed(x)) for x in ]

def apply_box(block_info, red, green, blue):
    t, green_x, green_y = block_info
    red = [[i for i in zip(*red)]]

    blue_x, blue_y = green_y, green_x

    depth = 0
    def apply_one_box(color_graph_x, color_graph_y, color_graph):
        depth = 0
        if t == 1:
            while depth < 6:
                if color_graph[depth][color_graph_y] == 0:
                    if depth == 5:
                        color_graph[depth][color_graph_y] = 1
                    depth += 1
                    break

                elif color_graph[depth][color_graph_y] != 0:
                    color_graph[depth-1][color_graph_y] = 1
                    break

        elif t == 2:
            while depth < 6:

                if not color_graph[depth][color_graph_y] and not color_graph[depth][color_graph_y+1]:
                    if depth == 5:
                        color_graph[depth][color_graph_y] = 1
                        color_graph[depth][color_graph_y+1] = 1
                    depth += 1
                
                elif color_graph[depth][color_graph_y] or color_graph[depth][color_graph_y+1]:
                    color_graph[depth-1][color_graph_y] = 1
                    color_graph[depth-1][color_graph_y+1] = 1
                    break
        
        elif t == 3:
            while depth < 5:
                if not color_graph[depth][color_graph_y] and not color_graph[depth+1][color_graph_y]:
                    if depth == 4:
                        color_graph[depth][color_graph_y] = 1
                        color_graph[depth+1][color_graph_y] = 1
                    depth += 1
                    break

                elif color_graph[depth][color_graph_y] or color_graph[depth+1][color_graph_y]:
                    color_graph[depth][color_graph_y] = 1
                    color_graph[depth+1][color_graph_y] = 1
                    break

        return color_graph

    green = apply_one_box(green_x, green_y, green)
    blue = apply_one_box(blue_x, blue_y, blue)

    print(green, blue)
    return green, blue
                    

def erase_row(graph):
    graph.pop()
    graph.appendleft()



    
# type 1: 블록 하나
# type 2: 블록 두개, 가로
# type 3: 블록 두개, 세로

if __name__ == '__main__':
    N = int(input())
    blocks = [list(map(int, input().split())) for _ in range(N)]
    green_graph = [[0 for _ in range(4)] for _ in range(6)]
    blue_graph = [[0 for _ in range(4)] for _ in range(6)]

    print(blocks)

    for block_info in blocks:
        print(f'block_info: {block_info}')
        green_graph, blue_graph = apply_box(block_info, green_graph, blue_graph)


        3,0 > 0,0
        1,3 > 3,2
        2,2 > 2,0
        2,3 > 3,0
