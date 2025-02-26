import praw
from config import config

reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    user_agent="my user agent",
)

for submission in reddit.subreddit("test").hot(limit=10):
    print(submission.title)
