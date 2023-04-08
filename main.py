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

#total number of posts in the liberal and conservative categories (change to command line arguement later, potentially)
NUM_POSTS = 1000
#location of training data
TRAINING_DATA = "/trainingData/"


def main():
    #loop through
    
    """Main Function."""


if __name__ == '__main__':
    main()