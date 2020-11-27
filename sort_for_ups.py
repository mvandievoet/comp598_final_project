import argparse
import json

def bubble_sort(lines):
	# We set swapped to True so the loop looks runs at least once
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(lines) - 1):
			dic1 = json.loads(lines[i])
			dic2 = json.loads(lines[i+1])
			if dic1['data']['ups'] > dic2['data']['ups']:
				# Swap the elements
				lines[i], lines[i + 1] = lines[i + 1], lines[i]
				# Set the flag to True so we'll loop again
				swapped = True

	return lines

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', dest='input_file', required=True)
	parser.add_argument('-o', dest='output_file', required=True)
	args = parser.parse_args()

	with open(f"{args.input_file}", 'r') as f:
		lines = f.readlines()

	#for line in lines:
	#	dic = json.loads(line)
	#	dic['data'].keys())
	lines = bubble_sort(lines)

	#for i in range(200,300):
	#	dic = json.loads(lines[i])
	#	print(dic['data']['ups'])
	arr = []
	for line in lines:
		dic = json.loads(line)
		arr.append(dic)

	with open(f"{args.output_file}", 'w') as f:
	        for dic in arr:
        		print(json.dumps(dic), file=f)

if __name__ == '__main__':
    	main()
