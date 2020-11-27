import requests
import json
import argparse

def get_posts(subreddit, num, after):
	data = requests.get(f'http://api.reddit.com{subreddit}/hot?limit={num}&after={after}',
		headers={'User-Agent': 'windows:requests (by /u/hdbois)'})
	return data.json()['data']

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-o', dest='output_file', required=True)
	parser.add_argument('subreddit')
	args = parser.parse_args()
	posts = []
	data = requests.get(f'http://api.reddit.com{args.subreddit}/hot?limit=99',
		headers={'User-Agent': 'windows:requests (by /u/hdbois)'})

	content = data.json()['data']
	posts.append(content['children'])
	after = content['after']

	for i in range(9):
		content = get_posts(args.subreddit, 100, after)
		posts.append(content['children'])
		after = content['after']

	# write each separate post on a new line
	with open(args.output_file, 'a') as outfile:
		for post in posts:
			for p in post:
				json.dump(p, outfile)
				outfile.write('\n')

if __name__ == '__main__':
    main()
