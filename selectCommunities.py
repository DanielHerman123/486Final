import argparse
import os
import sys
import praw
import shutil
import re

reddit = praw.Reddit(
    client_id='6wqQI91lq4Vp2YTxGl5JFw',
    client_secret='AfSw590WsCIQRgI5zZVM2p_ivPs6Sg',
    redirect_uri='http://localhost:8000',
    user_agent='486Final v1.0 - This app scrapes Reddit for data on a specific topic.'
)

def collect(amountTrain, community):
    """collect reddit posts"""

    # make call to api with provided communities


    # download to testing data directory
    subreddit = reddit.subreddit(community)
    with open(f'testingData/{community}.txt', mode='w') as f:
        for post in subreddit.new(limit=amountTrain):
            text = post.title
            if hasattr(post, 'selftext') and post.selftext != "":
                text += ' ' + post.selftext
            # Write row to .txt file
            text = re.sub(r"\n", " ", text)
            f.writelines(text)
            
            


def main(amountTrain, community):
    """Main Function."""

    #removes training data directory and then creates it 
    # for scraped data to go inside of
    if not os.path.exists('testingData'):
        os.mkdir('testingData')

    collect(int(amountTrain), community)

if __name__ == '__main__':
    #RUN WITHIN VIRTUAL ENVIRONMENT PIP INSTALL praw
    #RUN COMMAND IS: Python3 selectCommunities.py <amount int of data> <community>
    #Example: Python3 selectCommunities.py 1000 PoliticalDiscussion
    main(sys.argv[1], sys.argv[2])