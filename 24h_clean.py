import argparse
import json

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', dest='input_file', required=True)
	parser.add_argument('-o', dest='output_file', required=True)
	args = parser.parse_args()

	with open(f"{args.input_file}", 'r') as f:
		lines = f.readlines()	
	
	arr = []
	for line in lines:
		dic = json.loads(line)
	# 1606167540, 1606253940, 1606340340
		if dic['data']['created_utc'] > 1606436400:
			arr.append(dic)

	with open(f"{args.output_file}", 'w') as f:
	        for dic in arr:
        		print(json.dumps(dic), file=f)

if __name__ == '__main__':
    	main()
