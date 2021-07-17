

def search_next(i, j):
    next_nodes = [] 
    
    move = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]] # 上から時計回り
    
    # 隣接するノードをnext_nodesに格納する
    for k, l in move:
        if 0 <= i+k and i+k < h and 0 <= j+l and j+l < w: # out of range にならないように (0<=i+k<=h, 0<=j+l<=w-1)
            if (i+k, j+l) not in visited_nodes and (i+k, j+l) not in next_nodes and c[i+k][j+l] == 1: # visited_nodesとnext_nodesは重複させないほうがいい
                next_nodes.append((i+k, j+l)) 

    # next_nodesから1つ取り出し再帰
    while len(next_nodes) > 0:
        next_node = next_nodes.pop()
        i, j = next_node
        search_next(i, j)

    return 
