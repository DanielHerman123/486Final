import requests
import argparse
import os

# Parse command line arguments
parser = argparse.ArgumentParser(description='Scrape Reddit post text from specified communities and store them in a directory within the current directory')
parser.add_argument('communities', nargs='+', help='List of communities to scrape')
args = parser.parse_args()

# Set up Reddit API request headers and parameters
headers = {'User-Agent': 'MyBot/0.0.1'}
params = {'sort': 'top', 't': 'week', 'limit': 10}

# Create directory to store scraped text files
dir_name = 'reddit_scraped_text'
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

# Loop through specified communities
for community in args.communities:
    # Send Reddit API request to get top posts from past week
    url = f'https://www.reddit.com/r/{community}/top.json'
    response = requests.get(url, headers=headers, params=params)

    # Parse JSON response and loop through top posts to save text to file
    data = response.json()
    for post in data['data']['children']:
        text = post['data']['selftext']
        if text:
            filename = f"{dir_name}/{community}_{post['data']['id']}.txt"
            with open(filename, 'w') as f:
                f.write(text)