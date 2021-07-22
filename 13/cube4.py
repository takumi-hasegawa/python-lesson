def index_to_room_numbers(connected_index, rooms): # 部屋の座標集合から部屋番号の集合に変換するして返す
    C = set() #集合を定義
    for h, w in connected_index: # y,x座標を入れ,
        C |= set([rooms[h][w]]) # 部屋番号に変換してCに入れる

    return C

def node_connected_component(G, s): # 移れる部屋のりすとG,始点sから 繋がっている部屋の座標の集合を返す
    C = set([s]) # 集合を定義
    queue = [s] #始点からスタートして、移れる部屋を辿る これから辿るへやをキューにいれておく
    while len(queue) > 0: # 辿れる部屋がある限りループする
        v = queue.pop(0) # キューから1つ取り出し
        for node in G[v]: # 隣接頂点リストから取り出す
            if node not in C: # 未探索であれば
                C |= set([node]) #集合と
                queue.append(node) #キューに入れる
    return C

def solve(r, rooms):
    
    G = {(h, w): [] for h in range(r) for w in range(r)} # 部屋の座標をキー
    # 移れる部屋を値とする辞書で無向グラフを表す． 探索済みは1を入れる
    for h in range(r):
        for w in range(r):
            smallest_number = rooms[h][w] # ひとまずへやの最小数としておく あとで更新する

            # 4方向に移れる部屋があるか判定 現在の部屋より1大きければ移れる
            # 上,左,右,下の順で移れるか調べる
            if h > 0 and rooms[h - 1][w] - smallest_number == 1: #上の部屋のほうが1大きい場合
                smallest_number = rooms[h - 1][w] # smallest_numberを更新する
                movable = (h - 1, w) # 移れる部屋をmovableに入れる
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
                
    checked = [['' for w in range(r)] for h in range(r)] # checkedにはcheck済みの頂点に1をいれておく
    max_len = 0 # 最大で移れる部屋の数 初期値は0をいれておく
    win_room_number = float('inf') #勝者の部屋番号 初期値は大きい値入れておく
    for h in range(r):
        for w in range(r):
            if G[(h, w)] == 1: # check済みなら無視 次のループへ
                continue
            connected_index = node_connected_component(G, (h, w)) # 移動可能なroomの座標の集合を取得する
            connected_rooms = index_to_room_numbers(connected_index, rooms) # 上で得られた座標集合から部屋番号の集合に変換する
            for hh, ww in connected_index:
                G[(hh, ww)] = 1 # connectedに含まれればcheckedに追加

            if max_len < len(connected_rooms): # 移れる部屋の最大数を更新したら
                max_len = len(connected_rooms) # max_lenを更新する
                win_room_number = min(connected_rooms) # つながっている部屋の番号が一番小さいのが勝者 win_room_numberに入れる
            elif max_len == len(connected_rooms) and min(connected_rooms) < win_room_number: # 移れる部屋数同じで、部屋番号がより小さい場合
                win_room_number = min(connected_rooms) #部屋番号を更新する
                
    return win_room_number, max_len # 勝者のいた部屋、移れるへやの最大数を返す

T = int(input()) # Tをテストケースの数とする．
for case_number in range(1, T+1): # テストケース1からTまで繰り返す．
    while True: # 空白文字が入ってきたら無視する
        r = input() # 迷路の大きさはr^2になる rか空白文字が入ってくる
        if r: # rが空白文字でないなら
            r = int(r) # rは整数である
            break # rが入ったらループを抜ける

    rooms = [] # roomsに部屋番号を入れるつもり
    for i in range(r): # 1行ごとループ
        row = list(map(int, input().split())) # 一列ずつ
        rooms.append(row) #roomsに部屋番号を二次元配列として格納する
    room_num, max_move = solve(r, rooms) # 勝者の部屋番号、動ける部屋の最大数を取得
    print(f'Case #{case_number}: {room_num} {max_move}')