def reverse_sum(n):
    i=1
    reverse_sum = 0
    while True:
        reverse_sum += 1 / i
        if reverse_sum >= n:
            print(i)
            break
        i += 1

    return

reverse_sum(8)