'''
有向グラフでやってみる
(番号が小さい) ← (番号が大きい) みたいに向きをつけると 値を持たないところが候補になる？ 
'''

def get_min_number(connected_index, rooms):
    min_number = float('inf')
    for h, w in connected_index:
        if rooms[h][w] < min_number: min_number = rooms[h][w]
    return min_number

def node_connected_component(G, s):
    # つながっているnodeの集合を返したい、、、
    C = set([s])
    queue = [s]
    rooms_count = 0
    while len(queue) > 0:
        rooms_count += 1
        v = queue.pop()
        for node in G[v]: # 隣接頂点リストから取り出す
            if node not in C:
                C |= set([node])
                queue.append(node)
    return C, rooms_count

def solve(r, rooms):
    
    G = {(h, w): [] for h in range(r) for w in range(r)} # 頂点名をキー，
    # 移れる頂点のリストを値とする辞書で無向グラフを表す．探索済みなら1を入れる

    for h in range(r):
        for w in range(r):
            smallest_number = rooms[h][w]

            # 4方向に移れる部屋があるか判定 現在の部屋より1大きければ移れる
            # 上,左,右,下の順で移れるか調べる
            if h > 0 and rooms[h - 1][w] - smallest_number == 1: #上の部屋のほうが1大きい場合
                smallest_number = rooms[h - 1][w]
                movable = (h - 1, w)
            elif w > 0 and rooms[h][w - 1] - smallest_number == 1: #左の部屋のほうが1大きい場合
                smallest_number = rooms[h][w - 1]
                movable = (h, w - 1)
            elif w < r - 1 and rooms[h][w + 1] - smallest_number == 1: #右の部屋のほうが1大きい場合
                smallest_number = rooms[h][w + 1]
                movable = (h, w + 1)
            elif h < r - 1 and rooms[h + 1][w] - smallest_number == 1: #下の部屋のほうが1大きい場合
                smallest_number = rooms[h + 1][w]
                movable = (h + 1, w)

            if smallest_number != rooms[h][w]: # 移れる部屋があったら
                G[(h, w)].append(movable) # その部屋自分の隣接頂点に加え，
                G[movable].append((h, w)) # 同時に自分をその部屋の隣接頂点に加える．

    max_len = 0 #最大で移れる部屋の数 初期値は0をいれておく
    win_room_number = float('inf') #勝者の部屋番号 初期値はデカい数にしておく
    for h in range(r):
        for w in range(r):
            if G[(h, w)] == 1: # check済みなら無視 次のループへ
                continue
            connected_index, rooms_count = node_connected_component(G, (h, w)) # 移動可能なroomの座標の集合と, 連結数を取得
            for hh, ww in connected_index:
                G[(hh, ww)] = 1 # 探索済みにする
            if max_len > rooms_count: # 部屋の最大数が小さいなら調べる価値なし 次のループへ
                continue

            # 部屋数を同じか更新する場合のみ実行
            min_number = get_min_number(connected_index, rooms) # 最小番号を取得
            
            if max_len < rooms_count:
                max_len = rooms_count
                win_room_number = min_number
            elif max_len == rooms_count and min_number < win_room_number:
                win_room_number = min_number
                
    return win_room_number, max_len

T = int(input()) # Tをテストケースの数とする．
for case_number in range(1, T+1): # テストケース1からTまで繰り返す．
    r = int(input()) # 迷路の大きさはr^2になる
    rooms = [] # roomsに部屋番号を入れるつもり
    for i in range(r):
        row = list(map(int, input().split()))
        rooms.append(row) #roomsに部屋番号を二次元配列として格納する
    room_num, max_move = solve(r, rooms) 
    print(f'Case #{case_number}: {room_num} {max_move}')