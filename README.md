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
  - In R Studio install package tm, wordcloud
  - Edit RStudio to reflect path of csv file in relations to your working directory path
  - Compile to generate output (.png file)


Goals of this Project
  - To Identify public opinion/feeling towards a particular topic by analyzing commonly tweeted adjectives
  - Determine Publics overall status to the new Xbox console and analyze nouns and keywords to reflect consumer interest


Unmet Goals
  - Location based tracking (Not enough Data)
  - Sentence Structure Parsing and Analysis for further dissimenation
  - "Dial-in" gradient transitions of keywords with workcloud API

Large Spectrum Usages
  - Quickly and Efficiently Aggregate real-time twitter data for big picture snapshots of events, trends and other highly discussed developing issues/stories/events. From a market analysis this can derrive a snapshot of public opinion and gain insight on widely discussed issues going on in the world.
