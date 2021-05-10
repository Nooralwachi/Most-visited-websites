from collections import Counter
def most_visited_sites():
	result = {}
	with open("input.txt", "r") as f:
		for line in f:
			line=line.split()
			for l in line[1:]:
				if l in result:
					result[l] += 1
				else:
					result[l] = 1
	sorted_result = sorted(result.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
	if len(sorted_result) <= 5:
		print(sorted_result)
	else:
		for x,y in sorted_result[:5]:
			print(f'{x} {y}')

def most_visited_sites2():
	result = []
	with open("input.txt", "r") as f:
		for line in f:
			line=line.split()
			for l in line[1:]:
				result.append(l)
		print("---")
		websites=Counter(result)
		for k,v in websites.most_common(5):
			print(k,v)

most_visited_sites()
most_visited_sites2()
