import networkx as nx

while True:
    def shortest_path_length_without_nx(G, source, target):
        '''グラフ上の距離（最短路長）を返す関数
        入力は，グラフG，始点source，終点target，
        出力は，始点から終点へのグラフ上の距離，ただし始点と終点が同じ連結成分に含まれていない場合には-1'''
        C = set([source]) # 始点から到達可能であることがわかっている頂点集合をCとする．最初は始点のみが始点から到達可能であるとわかっている．
        queue = [source] # 幅優先探索なのでqueueに「探索境界上の頂点集合」を覚える．
        dist = {source: 0} # 始点からの距離をdistとする．最初は始点の，始点からの距離が0であることだけがわかっている．
        while len(queue) > 0: # queueに覚えられている「探索境界上の頂点」がある限り，以下を繰り返す．
            v = queue.pop(0) # 探索境界上の頂点を1つ抜き出す．
            for w in G[v]: # その頂点の隣接頂点wに関して，
                if w not in C: # wがすでに探索済みでないならば，
                    C |= set([w]) # 始点から到達可能であることを覚えて，
                    queue.append(w) # 「探索境界上の頂点」として覚えて，
                    dist[w] = dist[v] + 1 # 「頂点vへの距離+1」をその頂点wの距離とする．
        if target in C: # 終点が探索済みならば，始点と同じ連結成分に含まれているということなので，
            return dist[target] # 始点からの距離を返す．
        return -1 # そうでないならば，始点と終点が同じ連結成分に含まれていないということなので-1を返す


    w, h = map(int, input().split()) # wとｈを迷図の幅と高さとする．
    if w == 0 and h == 0: # 幅も高さも0ならば，
        break # 繰り返しを終える．
    G ={} 
    for i in range(h): 
        for j in range(w): 
            G[(i, j)] = []

    for i in range(h): # 迷図のそれぞれの縦位置iに関して，
        line = list(map(int, input().split())) # 横移動を阻む壁のデータを1行読み込み，
        for j in range(w - 1): # そのそれぞれの横位置jに関して，
            if line[j] == 0: # 右側に壁がないならば，右側との移動が可能なので，
                G[(i, j)].append((i, j+1)) # 頂点(i, j)と頂点(i, j + 1)をエッジで結ぶ．
                G[(i, j+1)].append((i, j)) 
        if i >= h - 1: continue # 以降は縦方向の移動に関するエッジの処理だが，縦位置が（０始まりなので）h-1だとそれよりも下がないので，以降の処理を省略する．
        line = list(map(int, input().split())) # 縦移動を阻む壁のデータを１行読み込み，
        for j in range(w): # そのそれぞれの横位置jに関して，
            if line[j] == 0: # 下側に壁がないならば，下側との移動が可能なので，
                G[(i, j)].append((i + 1, j)) # 頂点(i, j)と頂点(i + 1, j)をエッジで結ぶ．
                G[(i+1, j)].append((i, j)) # 頂点(i, j)と頂点(i + 1, j)をエッジで結ぶ．
    source = (0, 0) # 迷図の始点は常に(0, 0)
    target = (h - 1, w - 1) # 迷図の終点は常に(h - 1, w - 1)
    print(f'{shortest_path_length_without_nx(G, source, target) + 1}\n') # 始点から終点への，グラフ上の距離（最短路長）+1をファイルに出力する．