import os
import tweepy
from dotenv import load_dotenv
import sys
import json

#params:
#00 file_name
#01 track


load_dotenv()

consumer_key = os.environ["API_KEY"]
consumer_secret = os.environ["API_KEY_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuth1UserHandler(
  consumer_key,
  consumer_secret,
  access_token,
  access_token_secret
)

extracted_tweets = []


api = tweepy.API(auth)
max_tweets=100
query=sys.argv[1]
searched_tweets = [status._json for status in tweepy.Cursor(api.search_tweets,  q=query).items(max_tweets)]
json_strings = [json.dumps(json_obj) for json_obj in searched_tweets]


s=' '.join(str(v) for v in json_strings)
dest_file = "output_twitter.json"
with open(dest_file, "w") as f:
    f.write(s)
