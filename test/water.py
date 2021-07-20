def node_connected_component(G, s):
    ''' NetworkXのnode_connected_componentと同じ役割を果たす関数．
    ただし，入力のグラフは以下のsolutionで用意された形式に対応する． '''
    # これから作る予定
    # つながっているnodeの集合を返せればいい、、、
    C = set([s])
    # print(C)
    queue = [s]
    while len(queue) > 0:
        v = queue.pop(0)
        for node in G[v]: # 隣接頂点リストから取り出す
            if node not in C:
                C |= set([node])
                queue.append(node)
    return C


def solution(H, W, altitude):
    G = {(h, w): [] for h in range(H) for w in range(W)} # 頂点名をキー，
    # 隣接する頂点のリストを値とする辞書で無向グラフを表す．
    for h in range(H):
        for w in range(W):
            altitude_of_lowest_neighbor = altitude[h][w]
            if h > 0 and altitude[h - 1][w] < altitude_of_lowest_neighbor:
                altitude_of_lowest_neighbor = altitude[h - 1][w]
                neighbor = (h - 1, w)
            if w > 0 and altitude[h][w - 1] < altitude_of_lowest_neighbor:
                altitude_of_lowest_neighbor = altitude[h][w - 1]
                neighbor = (h, w - 1)
            if w < W - 1 and altitude[h][w + 1] < altitude_of_lowest_neighbor:
                altitude_of_lowest_neighbor = altitude[h][w + 1]
                neighbor = (h, w + 1)
            if h < H - 1 and altitude[h + 1][w] < altitude_of_lowest_neighbor:
                altitude_of_lowest_neighbor = altitude[h + 1][w]
                neighbor = (h + 1, w)
            if altitude_of_lowest_neighbor < altitude[h][w]: # ここまでで隣接する区画の高さが自分の区画よりも真に小さいならば，
                G[(h, w)].append(neighbor) # その一番低い区画を自分の隣接頂点に加え，
                G[neighbor].append((h, w)) # 同時に，自分を，その一番低い区画の隣接頂点に加える．
    unicode_point = ord('a')
    sol = [['' for w in range(W)] for h in range(H)]
    for h in range(H):
        for w in range(W):
            if sol[h][w] != '':
                continue
            comp = node_connected_component(G, (h, w)) # ここでは，上記の自作の関数で連結成分（の頂点集合）を得る．
            # print(comp)
            for hh, ww in comp:
                sol[hh][ww] = chr(unicode_point)
            unicode_point += 1
    return sol

T = int(input()) # Tをテストケースの数とする．
for case_number in range(1, T + 1): # テストケース1からTまで繰り返す．
    H, W = map(int, input().split()) # HとWを行数と列数とする．
    altitude = [] # altitudeにそれぞれの区画の高さを保存するつもり．
    for h in range(H):
        row = list(map(int, input().split()))
        altitude.append(row)
    sol = solution(H, W, altitude) # solution_with_nxで得られた，それぞれのテストケースの解をsolとする．
    print(f'Case #{case_number}:')
    for h in range(H): # 得られた解を，行ごとに，
        print(' '.join(sol[h])) # 空白を挟んで1つの文字列にして表示する