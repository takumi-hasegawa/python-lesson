def shortest_path_length(G, source, target):
    ''' NetworkXのshortest_path_lengthと同じ機能の関数を作る予定である．'''
    distance = {v: float('inf') for v in G.keys()}
    distance[source] = 0 # 始点から距離
    remain = [v for v in G.keys()] # 未探索

    while len(remain) > 0:
        min_dis = float('inf')
        for v in remain:
            if distance[v] < min_dis:
                min_dis = distance[v]
                min_dis_vertex = v
        if min_dis == float('inf'):
            break
        remain.remove(min_dis_vertex)
        for w in G[min_dis_vertex]:
            distance[w] = min(distance[w], distance[min_dis_vertex] + G[min_dis_vertex][w]) #隣接とどっちがでかいか？？

        if distance[target] == float('inf'):
            return -1

    return distance[target]