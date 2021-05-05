while True:
	n = int(input().rstrip())
	if n == 0:
		break

	an = list(map(int, input().split()))

	ave = sum(an) / len(an)

	num = 0
	for i in range(len(an)):
		if an[i] <= ave:
			num = num + 1

	print(num)