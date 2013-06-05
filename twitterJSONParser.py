#*********************
#Twitter API 1.1
#Parse Top 10 US Trend
#Carmine Valentino
#*********************

import oauth2 as oauth
import json, argparse, csv


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

#Twitter Parse
tweets = json.loads(data)
jsonData = tweets[0]

countJsonArray = 0

for n in tweets:
	if len(tweets[countJsonArray]) >= 1:
		countJsonArray = countJsonArray + 1

csv_file = open('/var/www/public/csv/' + jsonfile + ".csv", 'wb')
csv_write = csv.writer(csv_file)
	
headerString = ['text']
	
csv_write.writerow(headerString)


for i in range(0,countJsonArray):
	tweetDate = tweets[i]['created_at']
	tweetDate = unicode(tweetDate).encode("utf-8")
	tweetText = tweets[i]['text']
	tweetText = unicode(tweetText).encode("utf-8")

        tweetString = [tweetText]
	csv_write.writerow(tweetString)


print countJsonArray
