import praw
import structlog

from karma_farmer.core.config import config

reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    user_agent=f"python:karma-farmer (by /u/{config.username})",
)

log = structlog.get_logger()
