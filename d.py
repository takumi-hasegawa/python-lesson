count = 0
li = []
def calc_digits_product(num, count):
    count += 1

    if count > 4:
        return

    digits = []
    product = 1
    while num > 0:
        digits.append(num % 10)
        num //= 10

    for i in range(len(digits)):
        product *= digits[i]

    # print(product)
    
    if product > 10:
        calc_digits_product(product, count)
    else:
        if count == 4:
            global li
            li.append(1)

    return

# calc_digits_product(77, count)
# print(li)

maxnum = 1000000
for i in range(11, maxnum):
    calc_digits_product(i, count)
    
print(len(li))