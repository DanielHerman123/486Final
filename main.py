import requests
import argparse
import os
import praw

reddit = praw.Reddit(
    client_id='6wqQI91lq4Vp2YTxGl5JFw',
    client_secret='AfSw590WsCIQRgI5zZVM2p_ivPs6Sg',
    redirect_uri='http://localhost:8000',
    user_agent='486Final v1.0 - This app scrapes Reddit for data on a specific topic.'
)

#total number of posts in the liberal and conservative categories (change to command line arguement later, potentially)
NUM_POSTS = 1000
#location of training data
TRAINING_DATA = "/trainingData/"


def main():
    #loop through
    
    """Main Function."""


if __name__ == '__main__':
    main()