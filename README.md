twitter-public-survey
=====================

Collecting Twitter Data Using the Streaming API During the Xbox One Console Reveal to Derive Public Opinion

-Tweepy API (Python Package to Collect Streaming Twitter Data)

slistener.py/streaming.py Tweepy Script File
twitterStream.py (Not Used .. Initial Script to Determine GeoLocation from JSON)
twitterJSONParser.py Parses Twitter JSON File Collected from streaming.py and turns into CSV File with Timestamp and Tweet


Use Instructions
  - Install Tweepy Package using pip
  - Modify streaming.py to include Twitter OAUTH token and file save path
  - Execute streaming.py [#keyword] - Argument required to focus search on a word/words
  - After 10,000 Tweets have been collected a new file will be started with a unique timestamp (edit this in slistener.py)
  - twitterJSONParser.py [filepath.json] - Pass the json filename captured by streaming.py to this file to build the CSV file and Parse the JSON Data
