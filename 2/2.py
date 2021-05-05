while True:
	a = list(map(int, input().split()))
	n = a[0]
	m = a[1]
	if n == 0:
		break

	prices = list(map(int, input().split()))
	prices.sort()

	# for i in len(prices):
	# 	if prices[-1] >= m:
	# 		prices.pop()
	# 	else:
	# 		continue

	# print(prices)

	# # 要素数が2個未満の時は無理
	# if len(prices) < 2:
	# 	print("NONE")
	# 	continue
    
	max = 0
	# 要素数が2つ以上の時　前方から組み合わせる
	for i in range(len(prices) - 1):
		for j in range(len(prices) - i - 1):
			com = prices[i] + prices[j + i + 1]
			if m >= com > max:
			    max = com

	if max == 0:
		print("NONE")
		continue

	print(max)