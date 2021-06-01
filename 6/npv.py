def solution(M, C):

    # 現在価値
    def calcNpv(r, C) -> float:
        aggregateCFValue = 0
        for i in range(len(C)):
            if i == 0: # 初期投資の時だけマイナス
                aggregateCFValue -= C[i]
                continue # 2週目以降に飛ばす
            aggregateCFValue += C[i] / pow(1 + r, i) # 初期投資以降のCFを加算する. (1+rを用いて将来価値に直している)
        return aggregateCFValue
    

    # ここからメイン処理

    npv = calcNpv(0.12, C) # 中間の利子率を使用した時のCF価値を計算する

    return npv

T = int(input())
for case_number in range(1, T + 1):
    M = int(input())
    C = list(map(int, input().split()))
    print(f'Case #{case_number}: {round(solution(M, C), 9)}') 