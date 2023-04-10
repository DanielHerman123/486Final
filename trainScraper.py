import argparse
import os
import sys
import praw
import shutil
import csv

reddit = praw.Reddit(
    client_id='6wqQI91lq4Vp2YTxGl5JFw',
    client_secret='AfSw590WsCIQRgI5zZVM2p_ivPs6Sg',
    redirect_uri='http://localhost:8000',
    user_agent='486Final v1.0 - This app scrapes Reddit for data on a specific topic.'
)

def collect(amountTrain):
    """collect reddit posts"""

    # make call to api with provided communities
    communities_left = ['Democrats']    # should include more
    communities_right = ['Republican']

    # Prepare a CSV file for the combined data
    with open('trainingData/training_data.csv', mode='w', newline='', encoding='utf-8') as combined_file:
        combined_writer = csv.writer(combined_file)

        # Write header row for the CSV file
        combined_writer.writerow(['text', 'label'])

        # Loop through Left communities and download to trainingData directory
        for Lcommunity in communities_left:
            subreddit = reddit.subreddit(Lcommunity)
            for post in subreddit.new(limit=amountTrain):
                text = post.title
                if hasattr(post, 'selftext') and post.selftext != "":
                    text += '\n' + post.selftext
                # Write row to CSV file
                combined_writer.writerow([text, '0']) #left

        # Loop through Right communities and download to trainingData directory
        for Rcommunity in communities_right:
            subreddit = reddit.subreddit(Rcommunity)
            for post in subreddit.new(limit=amountTrain):
                text = post.title
                if hasattr(post, 'selftext') and post.selftext != "":
                    text += '\n' + post.selftext
                # Write row to CSV file
                combined_writer.writerow([text, '2']) # right

def main(amountTrain):
    """Main Function."""

    #removes training data directory and then creates it 
    # for scraped data to go inside of
    if os.path.exists('trainingData'):
        shutil.rmtree('trainingData')
    os.mkdir('trainingData')

    collect(int(amountTrain))

if __name__ == '__main__':
    #RUN WITHIN VIRTUAL ENVIRONMENT PIP INSTALL praw
    #RUN COMMAND IS: Python3 trainScraper.py <amount int of data for left and right>
    main(sys.argv[1])
