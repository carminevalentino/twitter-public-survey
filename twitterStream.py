#*********************
#Twitter API 1.1
#Parse Top 10 US Trend
#Carmine Valentino
#*********************

import oauth2 as oauth
import json, argparse


# Handle command line arguments
parser = argparse.ArgumentParser(description="Twitter 1.1 Stream Tweet Parser")
parser.add_argument('jsonfile', help="Specify the JSON file name")
args = parser.parse_args()
jsonfile = args.jsonfile


#Twitter OAUTH Keys
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

#Establish OAUTH Connection
consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

timeline_endpoint = "http://bls-serv1/public/json/" + jsonfile
response, data = client.request(timeline_endpoint)

#Return top 10 Twitter Trends in the US
tweets = json.loads(data)
jsonData = tweets[0]


for i in range(0, 240):
        tweetString = tweets[i]['coordinates']
	if tweetString is not "None":
		print tweets[i]['geo']
		#print "\n"
