import argparse
import os
import sys
import praw
import shutil

reddit = praw.Reddit(
    client_id='6wqQI91lq4Vp2YTxGl5JFw',
    client_secret='AfSw590WsCIQRgI5zZVM2p_ivPs6Sg',
    redirect_uri='http://localhost:8000',
    user_agent='486Final v1.0 - This app scrapes Reddit for data on a specific topic.'
)

def collect(amountTrain):
    """collect reddit posts"""
    # f = open('/trainingData', 'w')

    # make call to api with provided communities
    communities_left = ['Democrats']    # should include more
    communities_right = ['Republican']

    # Loop through Left communities and download to trainingData directory
    count = 0
    for Lcommunity in communities_left:
        subreddit = reddit.subreddit(Lcommunity)
        for post in subreddit.new(limit=amountTrain):
            # Check if post is a text post
            # if post.is_self:
            # Create filename based on post title
            filename = f"trainingData/left{count}.txt"
            # Write post text to file
            with open(filename, 'w') as f:
                f.write(post.title)
                if hasattr(post, 'selftext') and post.selftext != "":
                    print("left", count)
                    f.write('\n')
                    f.write(post.selftext)
                count += 1

    # Loop through Right communities and download to trainingData directory
    count = 0
    for Rcommunity in communities_right:
        subreddit = reddit.subreddit(Rcommunity)
        # print(subreddit)
        for post in subreddit.new(limit=amountTrain):
            # Check if post is a text post
            # if post.is_self:
            # print(post.selftext)
            # Create filename based on post title
            filename = f"trainingData/right{count}.txt"
            # Write post text to file
            with open(filename, 'w') as f:
                f.write(post.title)
                if hasattr(post, 'selftext') and post.selftext != "":
                    print("right", count)
                    f.write('\n')
                    f.write(post.selftext)
                count += 1

    # f.close()

def main(amountTrain):
    """Main Function."""

    #removes training data directory and then creates it 
    # for scraped data to go inside of
    if os.path.exists('trainingData'):
        shutil.rmtree('trainingData')
    os.mkdir('trainingData')

    collect(int(amountTrain))

if __name__ == '__main__':
    main(sys.argv[1])