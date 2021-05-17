def solve(n, score_list):
    score_list.sort() # 小さい順にソート
    min = score_list[0] # 最小値を取得
    max = score_list[-1] # 最大値を取得

    # 平均値を計算 
    # 分母はリストの合計から最大値、最小値を引いたもの
    # 分子はデータの個数から最大値、最小値の2分を引いたもの
    ave = (sum(score_list) - max - min) / (n - 2)

    return int(ave) #整数に変換しないと浮動小数点になる


def answer(input_file_name, output_file_name):
    input_file = open(input_file_name)
    output_file = open(output_file_name, 'w')
    while True: # とにかく繰り返す
        n = int(input_file.readline()) # 引数を整数にして返す関数intを利用
        if n == 0: # 審判数が0ならば，
            break # 繰り返しをやめる，すなわちこの関数を終了する．
        score = []
        for i in range(n):
            score = score + [int(input_file.readline())]
        output_file.write(str(solve(n, score)) + '\n')
    input_file.close()
    output_file.close()
    return