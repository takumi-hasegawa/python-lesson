import sys
points = []
n = 0
mode = 0

for line in sys.stdin.readlines():

	# nを入力
	if mode == 0:
		n = int(line.rstrip())
		if n == 0:
			break
		m = n # mは点数計算に使う
		mode = 1
		continue

	# n回appendする
	if mode == 1:
		num = int(line.rstrip())
		points.append(num)
		n = n - 1
		# append終了したら点数計算
		if n == 0:
			points.sort()
			max = points[0]
			min = points[-1]

			ave = (sum(points) - max - min) / (m - 2)

			print(int(ave))
			
			#初期化して次のループ
			n = 0
			mode = 0
			points.clear()
			continue


	# n > 0の間ループ
	# 配列に点数を突っ込む
	# for i in range(n):
	# 	num = int(line.rstrip())
	# 	points.append(num)
		

	# if n != 0:
	# 	num = int(line.rstrip())
	# 	points.append(num)
	# 	points.sort()
	# 	max = points[-1]
	# 	min = points[0]
	# 	print(points)
	# 	print(max)
	# 	print(min)
	# 	n = n - 1
	# else:
	# 	ave = (sum(points) - max - min) / 1
	# 	points.clear()

# while True:
# 	n = int(input().rstrip())
# 	for i in range(n):
# 		num = input().rstrip()
# 		points.append(num)
	