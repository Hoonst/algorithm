for i in range(3):
    for j in range(4):
        print(i,j)
        flag = 0
        if j == 3:
            flag = 1
            break    
    if flag:
        break