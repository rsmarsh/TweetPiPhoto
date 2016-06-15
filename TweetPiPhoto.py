import time
import tweepy
import random
from picamera import PiCamera
		
#replace the following with the API keys for the account you wish the tweets to be sent from
consumer_key = 'REPLACE'
consumer_secret = 'REPLACE'
access_token = 	'REPLACE'
access_token_secret = 'REPLACE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Edit this variable with the message you want to follow after the @user tag.
message_with_photo = 'Here is your photo!'

"""
NOT YET IMPLEMENTED, IGNORE
#array of preset messages to follow the @username in the tweet
random_tweet_text: ['Look at this photo',
					'THESE',
					'WITH',
					'YOUR',
					'DESIRED TWEET TEXTS',
											
					]

"""
camera = PiCamera()

#if your images are upside down, then uncomment the line below
#camera.rotation = 180


def take_photo(tweet_from):
	original_author = tweet_from
]	photo_file_name = str(time.time())+'-'+original_author
	photo_file_extension = 'jpg'
	filepath = 'images/'+photo_file_name+'.'+photo_file_extension
	camera.capture('images/'+photo_file_name+'.'+photo_file_extension)
	
	upload_photo(filepath, original_author)
	
def upload_photo(filepath, original_author):
	send_to = original_author
	photo = filepath
	status = '@'+original_author+' '+message_with_photo
	api.update_with_media(photo, status=status)
	
	
class MyStreamListener(tweepy.StreamListener):
	
	#activated when a status matches
	def on_status(self, status):
		print(status.user.screen_name)
		print(status.text)
		tweet_from = status.user.screen_name
		take_photo(tweet_from)
		#print(status)
		
	def on_error(self, status_code):
		if status_code == 420:
			print('420 error')
			return False
			
			
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

""""
*********************************************************************************************
enter the keyword here which you wish the program to watch for on Twitter
e.g. '#LondonWeatherUpdate' or 'New House Building Update' or '@watchingpaintdrylive'
keyword_to_watch = '#TweetPiPhoto'
*********************************************************************************************
"""
keyword_to_watch = 'REPLACE WITH DESIRED TERM'

myStream.filter(track=[keyword_to_watch], async=True)


