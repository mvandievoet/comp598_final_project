import argparse
import json

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', dest='input_file', required=True)
	parser.add_argument('-o', dest='output_file', required=True)
	args = parser.parse_args()

	with open(f"{args.input_file}", 'r') as f:
		lines = f.readlines()	
	

	indexes = []
	n = len(lines)
	i = 0
	while i < n-1 :
		dic1 = json.loads(lines[i])
		j = i + 1
		while j < n:
			dic2 = json.loads(lines[j])
			if dic1['data']['id'] == dic2['data']['id']:
				indexes.append(j)
			j = j + 1
		i = i + 1
	
	arr = []
	lines = [i for j, i in enumerate(lines) if j not in indexes]
	for line in lines:
		arr.append(json.loads(line))

	with open(f"{args.output_file}", 'w') as f:
	        for dic in arr:
        		print(json.dumps(dic), file=f)

if __name__ == '__main__':
    	main()
