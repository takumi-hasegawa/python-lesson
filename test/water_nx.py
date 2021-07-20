import networkx as nx

def solution_with_nx(H, W, altitude):
    G = nx.Graph() # 空の無向グラフをGとする．
    for h in range(H): # それぞれの行hに関して，
        for w in range(W): # それぞれの列wに関して，
            altitude_of_lowest_neighbor = altitude[h][w] # 以降で「自分よりも低い隣りの区画の中で最も低い区画」を見つけるために，
            # 区画(h, w)の高さをaltitude_of_lowest_neighborの初期値とする．
            if h > 0 and altitude[h - 1][w] < altitude_of_lowest_neighbor:
                # 最北の区画ではなくて，かつ，北隣の区画が自分よりも低いならば，
                altitude_of_lowest_neighbor = altitude[h - 1][w] # 北隣の高さが「最低」であると一旦仮定して，
                neighbor = (h - 1, w) # 北隣へ水が流れると一旦仮定する．
            if w > 0 and altitude[h][w - 1] < altitude_of_lowest_neighbor:
                # 最西の区画ではなくて，かつ，西隣の区画が，「自分及び北隣」よりも低いならば，
                altitude_of_lowest_neighbor = altitude[h][w - 1] # 西隣の高さが「最低」であると一旦仮定して，
                neighbor = (h, w - 1) # 西隣へ水が流れると一旦仮定する．
            if w < W - 1 and altitude[h][w + 1] < altitude_of_lowest_neighbor:
                # 最東の区画ではなくて，かつ，西隣の区画が，「自分，北隣，西隣」よりも低いならば，
                altitude_of_lowest_neighbor = altitude[h][w + 1] # 東隣の高さが「最低」であると一旦仮定して，
                neighbor = (h, w + 1) # 東隣へ水が流れると一旦仮定する．
            if h < H - 1 and altitude[h + 1][w] < altitude_of_lowest_neighbor:
                # 最南の区画ではなくて，かつ，西隣の区画が，「自分，北隣，西隣，東隣」よりも低いならば，
                altitude_of_lowest_neighbor = altitude[h + 1][w] # 南隣の高さが「最低」であると一旦仮定して，
                neighbor = (h + 1, w) # 南隣へ水が流れると一旦仮定する．
            if altitude_of_lowest_neighbor == altitude[h][w]: # ここまでで「最低」の高さが自分の高さならば，自分の区画が「池」なので，
                G.add_node((h, w)) # グラフに，自分の区画に対応する頂点を加えるに留める．
            else: # そうでないならば，neighborに水が流れる先が記憶されているはずなので，
                G.add_edge((h, w), neighbor) # 自分と「水が流れる先」を結ぶエッジを加える．
                # NetworkXのadd_edgeは，エッジの端点の頂点がないならば，頂点も加えてくれることに注意されたい．
    unicode_point = ord('a') # 組み込み関数ordは，引数の文字の「Unicodeにおける番号」を返す．
    sol = [['' for w in range(W)] for h in range(H)] # 空文字列を成分とする行列（リストのリスト）を解の初期値とする．
    for h in range(H): # それぞれの行hに関して，
        for w in range(W): # それぞれの列wに関して，
            if sol[h][w] != '': # すでに解として何らかの文字が設定されているならば，
                continue # いずれかの「池」に属すると判定されたあとなので，処理を省略する．
            comp = nx.node_connected_component(G, (h, w)) # 区画(h, w)が属するグラフ連結成分（の頂点集合）をcompとする．
            print(comp)
            for hh, ww in comp: # その連結成分の頂点に対応する区画それぞれに，
                sol[hh][ww] = chr(unicode_point) # 現在のUnicode番号の文字を書き込み，
            unicode_point += 1 # Unicode番号を1増やす．すなわち，アルファベット順で次の文字の番号にする．
    return sol # こうして作った行列（リストのリスト）を返す．


T = int(input()) # Tをテストケースの数とする．
for case_number in range(1, T + 1): # テストケース1からTまで繰り返す．
    H, W = map(int, input().split()) # HとWを行数と列数とする．
    altitude = [] # altitudeにそれぞれの区画の高さを保存するつもり．
    for h in range(H):
        row = list(map(int, input().split()))
        altitude.append(row)
    sol = solution_with_nx(H, W, altitude) # solution_with_nxで得られた，それぞれのテストケースの解をsolとする．
    print(f'Case #{case_number}:')
    for h in range(H): # 得られた解を，行ごとに，
        print(' '.join(sol[h])) # 空白を挟んで1つの文字列にして表示する