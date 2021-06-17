num = 1234567890
maxnum = 30000000
# num = 1000
# maxnum = 300

divisors = []

for i in range(1, maxnum+1):
    if num % i == 0 and num % i <= maxnum:
        divisors.append(i)

print(divisors)
print(sum(divisors))
