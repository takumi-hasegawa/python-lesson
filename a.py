def yonjyou(n):
    num = n**4
    return num

def wa(num):
    wa = 0
    for i in range(1, num+1):
        wa += yonjyou(i)
    return wa

print(wa(64))