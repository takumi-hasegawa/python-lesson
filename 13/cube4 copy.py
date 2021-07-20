def index_to_room_numbers(connected_index, rooms):
    C = set()
    for h, w in connected_index:
        C |= set([rooms[h][w]])

    return C

def node_connected_component(G, s):
    # つながっているnodeの集合を返したい、、、
    C = set([s])
    queue = [s]
    while len(queue) > 0:
        v = queue.pop(0)
        for node in G[v]: # 隣接頂点リストから取り出す
            if node not in C:
                C |= set([node])
                queue.append(node)
    return C

def solve(r, rooms):
    for h in range(r):
        for w in range(r):
            current_number = rooms[h][w]
            next_node = []
            # 4方向に移れる部屋があるか判定 現在の部屋より1大きければ移れる
            # 上,左,右,下の順で移れるか調べる
            if h > 0 and rooms[h - 1][w] - current_number == 1: #上の部屋のほうが1大きい場合
                current_number = rooms[h - 1][w]
                movable = (h - 1, w)
            elif w > 0 and rooms[h][w - 1] - current_number == 1: #左の部屋のほうが1大きい場合
                current_number = rooms[h][w - 1]
                movable = (h, w - 1)
            elif w < r - 1 and rooms[h][w + 1] - current_number == 1: #右の部屋のほうが1大きい場合
                current_number = rooms[h][w + 1]
                movable = (h, w + 1)
            elif h < r - 1 and rooms[h + 1][w] - current_number == 1: #下の部屋のほうが1大きい場合
                current_number = rooms[h + 1][w]
                movable = (h + 1, w)

            if smallest_number != rooms[h][w]: # 移れる部屋があったら
                G[(h, w)].append(movable) # その部屋自分の隣接頂点に加え，
                G[movable].append((h, w)) # 同時に自分をその部屋の隣接頂点に加える．
                
    checked = [['' for w in range(r)] for h in range(r)] # checkedにはcheck済みの頂点に1をいれておく
    max_len = 0 #最大で移れる部屋の数 初期値は0をいれておく
    win_room_number = float('inf') #勝者の部屋番号 初期値はクソデカ
    for h in range(r):
        for w in range(r):
            if checked[h][w] == 1: # check済みなら無視 次のループへ
                continue
            connected_index = node_connected_component(G, (h, w)) # 移動可能なroomの座標の集合を取得する
            connected_rooms = index_to_room_numbers(connected_index, rooms)
            for hh, ww in connected_index:
                checked[hh][ww] = 1 # connectedに含まれればcheckedに追加

            if max_len < len(connected_rooms):
                max_len = len(connected_rooms)
                win_room_number = min(connected_rooms)
            elif max_len == len(connected_rooms) and min(connected_rooms) < win_room_number:
                win_room_number = min(connected_rooms)
                
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