import os
from dataclasses import dataclass


@dataclass
class Config:
    client_id = os.environ["KARMA_FARMER_CLIENT_ID"]
    client_secret = os.environ["KARMA_FARMER_CLIENT_SECRET"]
    username = os.environ["KARMA_FARMER_USERNAME"]


config = Config()
