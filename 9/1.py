import networkx as nx

while True:
    w, h = map(int, input().split()) # wとｈを迷図の幅と高さとする．
    if w == 0 and h == 0: # 幅も高さも0ならば，
        break # 繰り返しを終える．
    G = nx.Graph() # 空のグラフをGとする．
    for i in range(h): # 迷図のそれぞれの縦位置iと，
        for j in range(w): # 横位置jに関して，
            G.add_node((i, j)) # そのマス目に対応する頂点(i, j)をグラフに加える．
    for i in range(h): # 迷図のそれぞれの縦位置iに関して，
        line = list(map(int, input().split())) # 横移動を阻む壁のデータを1行読み込み，
        for j in range(w - 1): # そのそれぞれの横位置jに関して，
            if line[j] == 0: # 右側に壁がないならば，右側との移動が可能なので，
                G.add_edge((i, j), (i, j + 1)) # 頂点(i, j)と頂点(i, j + 1)をエッジで結ぶ．
        if i >= h - 1: continue # 以降は縦方向の移動に関するエッジの処理だが，縦位置が（０始まりなので）h-1だとそれよりも下がないので，以降の処理を省略する．
        line = list(map(int, input().split())) # 縦移動を阻む壁のデータを１行読み込み，
        for j in range(w): # そのそれぞれの横位置jに関して，
            if line[j] == 0: # 下側に壁がないならば，下側との移動が可能なので，
                G.add_edge((i, j), (i + 1, j)) # 頂点(i, j)と頂点(i + 1, j)をエッジで結ぶ．
    source = (0, 0) # 迷図の始点は常に(0, 0)
    target = (h - 1, w - 1) # 迷図の終点は常に(h - 1, w - 1)
    if nx.has_path(G, source, target) == False: # まず，始点から終点へのパスがないならば，
        print(0) # ファイルに0と出力する．
    else: # そうではなく，始点から終点へのパスがあるならば，
        print(f'{nx.shortest_path_length(G, source, target) + 1}\n') # 始点から終点への，グラフ上の距離（最短路長）+1をファイルに出力する．