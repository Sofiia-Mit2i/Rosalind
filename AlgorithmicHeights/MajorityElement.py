from collections import Counter

def MajorityELement(file_path):
	with open (file_path, 'r') as file:
		conditions = file.readline().split()
		lines = conditions[0]
		print(lines)
		size = int(conditions[1])
		check = size//2
		majorities = []

		for line in file:
			lineinprocess = line.split()
			integerline = [int(num) for num in lineinprocess] 
			counts = Counter(integerline)

			for num, freq in counts.items():
				if freq > check:
					majorities.append(num)
					break
			else:
				majorities.append(-1)

		return majorities

file_path = input('Please enter a path to your data: ')
answer = MajorityELement(file_path)
print(*answer)