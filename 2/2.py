while True:
	a = list(map(int, input().split()))
	n = a[0]
	m = a[1]
	if n == 0:
		break

	max = 0
	prices = list(map(int, input().split()))
	prices.sort()
	prices.reverse()

	# anがmより大きければ削除
	for i in range(len(prices)):
		if prices[i] >= m:
			prices[i].pop(i)

	# 要素数が2個未満の時は無理
	if len(prices) < 2:
		print("NONE")
		continue

	# 要素数が2つ以上の時　前方から組み合わせる
	for i in range(len(prices) - 1):
		for j in range(len(prices) - i - 1):
			com = prices[i] + prices[j + i + 1]
			print(com)
