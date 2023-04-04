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

