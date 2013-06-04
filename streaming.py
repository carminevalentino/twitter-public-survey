#*********************************
#Twitter API 1.1/Tweepy API
#Collect Real-Time Streaming
#Twitter Data Passed Through Arg
#*********************************

from slistener import SListener
import time, tweepy, sys, argparse

## authentication
consumer_token  = ''
consumer_secret = ''
access_token    = ''
access_secret   = ''

auth     = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_secret)
api      = tweepy.API(auth)

def main():
# Handle command line arguments
    parser = argparse.ArgumentParser(description="Twitter 1.1 Stream Tweet Collector Using Tweepy")
    parser.add_argument('hashtag', help="Specify the keyword or hashtag you wish to return")
    args = parser.parse_args()
    hashtag = args.hashtag

#Begin script

    track = [hashtag]
    
    listen = SListener(api, hashtag)
    stream = tweepy.Stream(auth, listen)

    print "Streaming started ..."

    try: 
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()
