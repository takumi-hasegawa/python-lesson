def solve(n, score_list):
	return score_list

def answer():
	input_file = open('A1')
	lines = input_file.readlines()
	input_file.close()
	while True:

		n = int(lines[0])
		if n == 0:
			break
		lines =lines[1:]
		print(solve(n, lines[:n]))
		lines = lines[n:]
	return lines