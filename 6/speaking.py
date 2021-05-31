ge_dict = {' ': ' ',
 'a': 'y',
 'b': 'h',
 'c': 'e',
 'd': 's',
 'e': 'o',
 'f': 'c',
 'g': 'v',
 'h': 'x',
 'i': 'd',
 'j': 'u',
 'k': 'i',
 'l': 'g',
 'm': 'l',
 'n': 'b',
 'o': 'k',
 'p': 'r',
 'r': 't',
 's': 'n',
 't': 'w',
 'u': 'j',
 'v': 'p',
 'w': 'f',
 'x': 'm',
 'y': 'a'}

T = int(input()) # 1行標準入力から読み込んで，それをテストケース数とする．
for t in range(T): # テストケース数だけ繰り返す．
    google_string = input() # グーグル語の文字列を1行読み込む．
    english_string = '' # 英語文字列を空文字列として初期化する．
    for g in google_string: # グーグル語のそれぞれの文字gに関して，
        english_string += ge_dict[g] # グーグル語のgに対応する英文字を末尾に加える．
    print(f'Case #{t + 1}: {english_string}') # こうしてできた英文字列を解答として標準出力に表示する．