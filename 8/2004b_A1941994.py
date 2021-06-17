while True:

    def search_tiles(x, y): #現在地点の隣接タイルを判定する
        visited_tiles.append((x, y)) # 現在地点をvisited_tilesに追加

        for i, j in moves: # 隣接タイルが移動可能であったらnext_tilesに座標を入れる
            if 0 <= x+i and x+i < w and 0 <= y+j and y+j < h: # out of rangeにならないように
                if (x+i, y+j) not in visited_tiles and (x+i, y+j) not in next_tiles and tiles[y+j][x+i] == ".":
                    next_tiles.append((x+i, y+j))
        
        while len(next_tiles) > 0: # next_tilesがなくなるまで再帰
            next_tile = next_tiles.pop() # next_tilesの末尾から1つ座標を取り出す
            i, j = next_tile
            search_tiles(i, j) # next_tilesの末尾の座標を現在地点とし、再帰
        
        return

    w, h = map(int, input().split()) # 幅w,高さhを取得
    if w == 0: #wが0なら終了
        break

    tiles = [] # 部屋のタイルを格納する配列
                # ※tiles[y座標][x座標]になる

    for i in range(h): #hの分だけtilesにappendする
        line = input().rstrip()
        tiles.append(line)

        if "@" in line: # 現在位置(@)が何行目にあったか記憶する
            current_y = i # @のy座標
            current_x = line.find("@") # @のx座標

    visited_tiles = [] # 移動したタイル
    next_tiles = [] # 移動する予定のタイル
    # move = [[0, -1], [-1, 0], [0, 1], [1, 0]] # 隣接4方向の座標
    moves = [(0, -1), (-1, 0), (0, 1), (1, 0)] # 隣接4方向の座標

    search_tiles(current_x, current_y)

    print(len(visited_tiles))