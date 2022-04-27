dx = [1,-1,0,0]
dy = [0,0,1,-1]

def batch_function(student_info, graph):
    N = len(graph)
    for student in student_info:
        student_id, favorites = student[0], student[1:]
        
        candidate = []

        max_neighbor = 0

        for row_idx in range(N):
            for col_idx in range(N):
                if graph[row_idx][col_idx] == 0:
                    blank = 0
                    neighbor = 0
                    for i in range(4):
                        moved_x = row_idx + dx[i]
                        moved_y = col_idx + dy[i]
                        if 0 <= moved_x < N and 0 <= moved_y < N:
                            if graph[moved_x][moved_y] in favorites:
                                neighbor += 1
                            elif graph[moved_x][moved_y] == 0:
                                blank += 1

                    if neighbor >= max_neighbor:
                        max_neighbor = neighbor
                        candidate.append([neighbor, blank, row_idx, col_idx])

        first_neighbor = sorted([n for n in candidate if n[0] == max_neighbor], key = lambda x: (-x[0], -x[1], x[2], x[3]))[0]
        _, _, first_x, first_y = first_neighbor

        graph[first_x][first_y] = student_id
        
    return graph           

def point_function(student_info, graph):
    N = len(graph)

    points = {0:0, 1:1, 2:10, 3:100, 4:1000}
    total_point = 0
    for row_idx in range(N):
        for col_idx in range(N):
            point = 0
            favorites = student_info[graph[row_idx][col_idx]]
            for i in range(4):
                moved_x = row_idx + dx[i]
                moved_y = col_idx + dy[i]
                
                if 0 <= moved_x < N and 0 <= moved_y < N:
                    if graph[moved_x][moved_y] in favorites:
                        point += 1
            total_point += points[point]

    return total_point

if __name__ == '__main__':
    N = int(input())
    student_info = [list(map(int, input().split())) for _ in range(N**2)]

    graph = [[0 for _ in range(N)] for _ in range(N)]
    graph = batch_function(student_info, graph)

    student_info = {key: [a,b,c,d] for key,a,b,c,d in student_info}
    point = point_function(student_info, graph)

    print(point)