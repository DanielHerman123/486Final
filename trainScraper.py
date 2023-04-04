import requests
import argparse
import os
import praw

reddit = praw.Reddit(
    client_id='your_client_id',
    client_secret='your_client_secret',
    redirect_uri='http://localhost:8000',
    user_agent='your_user_agent'
)

def collect():
    """collect reddit posts"""
    # f = open('/trainingData', 'w')

    # make call to api with provided communities
    communities_left = ['Democrats']    # should include more
    communities_right = ['Republican']

    # Loop through Left communities and download to trainingData directory
    count = 0
    for Lcommunity in communities_left:
        subreddit = reddit.subreddit(Lcommunity)
        for post in subreddit.new(limit=10):
            # Check if post is a text post
            if post.is_self:
                # Create filename based on post title
                filename = f"/trainingData/left{count}.txt"
                # Write post text to file
                with open(filename, 'w') as f:
                    f.write(post.selftext)
                    count += 1

    # Loop through Right communities and download to trainingData directory
    count = 0
    for Rcommunity in communities_right:
        subreddit = reddit.subreddit(Lcommunity)
        for post in subreddit.new(limit=10):
            # Check if post is a text post
            if post.is_self:
                # Create filename based on post title
                filename = f"/trainingData/left{count}.txt"
                # Write post text to file
                with open(filename, 'w') as f:
                    f.write(post.selftext)
                    count += 1

    # f.close()

def main():
    """Main Function."""

    #removes training data directory and then creates it 
    # for scraped data to go inside of
    if os.path.exists('/trainingData'):
        os.rmdir('/trainingData')
    os.mkdir('/trainingdata')

    collect()

if __name__ == '__main__':
    main()