def solution(M, C):

    ### 方針
    # 利子率 -1<r<1
    # r=0代入し、キャッシュフロー総(将来)価値と0の大小を調べる
    # 

    # 中間の利子率とCFからキャッシュフロー価値を計算する関数
    def calcAggregateCFValue(r, C) -> float:
        aggregateCFValue = 0
        for i in range(len(C)):
            if i == 0: # 初期投資の時だけマイナス
                aggregateCFValue -= C[i] * pow(1 + r, len(C) - i - 1)
                continue # 2週目以降に飛ばす
            aggregateCFValue += C[i] * pow(1 + r, len(C) - i - 1) # 初期投資以降のCFを加算する. (1+rを用いて将来価値に直している)
        return aggregateCFValue
    

    # ここからメイン処理
    
    upper_interest = 1 # 初期の利子率上限
    lower_interest = -1 # 下限

    while float(upper_interest) - float(lower_interest) > 0.0000000001: # 小数点9桁が正確に求まるまで繰り返す

        mid_interest = float((upper_interest + lower_interest) / 2) # 中間の利子率求める

        aggregateCFValue = calcAggregateCFValue(mid_interest, C) # 中間の利子率を使用した時のCF価値を計算する

        if aggregateCFValue >= 0: # CF価値が0以上なら、IRRとなる利子率はmid_interestより高いところにある
            lower_interest = mid_interest # 下限を更新
        else: # CF価値が0未満なら、IRRとなる利子率はmid_interestより低いところにある
            upper_interest = mid_interest # 上限を更新

    sol = upper_interest # 下限と上限どっちを代入してもいい

    return sol


T = int(input())
for case_number in range(1, T + 1):
    M = int(input())
    C = list(map(int, input().split()))
    print(f'Case #{case_number}: {round(solution(M, C), 9)}')