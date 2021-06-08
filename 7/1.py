while True:
    def graph_scanning_dict(G, s): # ここでGは頂点隣接リストの辞書表現である．
        visited_nodes = set([s])
        boundary_nodes = set([s])
        while len(boundary_nodes) > 0:
            v = boundary_nodes.pop()
            for w in G[v]: # graph_scanningと異なるのは，ここだけである．
                if w not in visited_nodes:
                    visited_nodes |= set([w])
                    boundary_nodes |= set([w])
        return visited_nodes

    def number_connected_components_dict(G): # ここでもGは頂点隣接リストの辞書表現である．
        scanned_nodes = set([])
        remaining_nodes = set(G.keys()) # まだ吟味していない頂点の集合をGの頂点集合そのものとする．
        # 辞書のメソッドkeys()ですべてのキーが得られる．そしてこの場合，それがグラフの頂点集合になっている．
        num = 0
        while len(remaining_nodes) > 0:
            v = remaining_nodes.pop()
            num += 1
            visited_nodes = set(graph_scanning_dict(G, v))
            scanned_nodes |= visited_nodes
            remaining_nodes -= visited_nodes
            return num

    w, h = map(int, input().split()) # 標準入力からデータを受け取る．
    if w == 0 and h == 0:
        break
    c = []
    for i in range(h):
        c.append(list(map(int, input().split())))
    G = {} # 空の辞書だが，これは空の頂点隣接リストというつもりである．
    for i in range(h):
        for j in range(w):
            if c[i][j] == 1:
                G[(i, j)] = []


    # 1のところの隣接点を表すリストGに追加していく
    for i in range(h):
        for j in range(w):
            if j < w - 1 and c[i][j] == 1 and c[i][j + 1] == 1: # 右側が1かを判定
                G[(i, j)].append((i, j + 1)) # 頂点(i, j)の隣接頂点として(i, j + 1)を追加
                G[(i, j + 1)].append((i, j)) # と同時に，頂点(i, j + 1)の隣接頂点として(i, j)を追加することを忘れない．
            if i < h - 1 and c[i][j] == 1 and c[i + 1][j] == 1: # 下が1か判定
                G[(i, j)].append((i + 1, j))
                G[(i + 1, j)].append((i, j))
            if i < h - 1 and j > 0 and c[i][j] == 1 and c[i + 1][j - 1] == 1: # 左下判定
                G[(i, j)].append((i + 1, j - 1))
                G[(i + 1, j - 1)].append((i, j))
            if i < h - 1 and j < w - 1 and c[i][j] == 1 and c[i + 1][j + 1] == 1: # 右下判定
                G[(i, j)].append((i + 1, j + 1))
                G[(i + 1, j + 1)].append((i, j))

    print(f'{number_connected_components_dict(G)}')