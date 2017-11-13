import time
import tweepy
import random
import os
import setup as program_data
from picamera import PiCamera

#iterate through the provided messages, and remove any which are longer than the maximum tweet length
def remove_long_messages(message_array):

	#this is -17 because it includes the '@' symbol, the maximum username length of 15, and a single space
	maximum_length = 280-17

	#if the account has been enabled to use the new 280 character limit
	if not program_data.enable_long_tweets:
		maximum_length = 140-17

	for message in message_array:
		#if the message is longer than the maximum twitter length
		
		if len(message) > maximum_length:
			print('The message: \'' + message + ' is too long, and will not be included')
			message_array.remove(message)

	return message_array


#returns a random string from the array in setup.py
#if set to not use any message, then just use a blank string
def get_random_tweet_message():
	if not program_data.send_message_with_tweet:
		return ''
	else:
		return random.choice(tweet_messages)

#this is called when the keyword has been detected.
#the tweet_from argument will be the username of whoever posted the keyword to Twitter
def take_photo(tweet_from):
	original_author = tweet_from

	#file name example: '2017Nov09-225130-Tweeter', date + time with seconds
	photo_file_name = time.strftime('%Y%b%d-%H%M%S')+'-'+original_author
	photo_file_extension = 'jpg'
	filepath = program_data.filepath+photo_file_name+'.'+photo_file_extension
	camera.capture('images/'+photo_file_name+'.'+photo_file_extension)
	
	upload_photo(filepath, original_author)

#used to delete a photo after it has been posted to Twitter, if the user has set save_image_locally to False
def delete_photo(filepath):
	if os.path.exists(filepath):
		os.remove(filepath)


#receives the location and name of the image as one string, and the twitter user to respond to
#this then intiates the upload and then automatically posts the tweet
def upload_photo(filepath, original_author):

	#grab a random message from the array of messages provided in setup.py
	message_with_photo = get_random_tweet_message()

	#attaches the username to the start or end of the tweet, depending on the user's preference
	if program_data.attach_username_to_end and program_data.send_message_with_tweet:
		status = message_with_photo+' @'+original_author
	else: 
		status = '@'+original_author+' '+message_with_photo
		
	api.update_with_media(filepath, status=status)

	#the image must be initially saved for the photo post to work, but it will be deleted if saving is set to False
	if not program_data.save_image_locally:
		delete_photo(filepath)
	
class MyStreamListener(tweepy.StreamListener):
	
	#activated when a status matches the keyword
	def on_status(self, status):
		print('keyword match by: ')
		print(status.user.screen_name)
		print(status.text)
		take_photo(status.user.screen_name)
		print('image response successfully tweeted!')
		
	def on_error(self, status_code):
		#error 420 is caused when the account triggers the rate limitations of twitter by tweeting too often
		if status_code == 420:
			print('420 error, this is caused by the rate limiter. try a new more unique keyword if this becomes an issue')
			return False
		else:
			print(str(status_code) + ' error')


#the API keys for the account you wish the tweets to be sent from
consumer_key = program_data.consumer_key
consumer_secret = program_data.consumer_secret
access_token = 	program_data.access_token
access_token_secret = program_data.access_token_secret

#if one of the Twitter keys required to operate are missing, then terminate the program
if not consumer_key or not consumer_secret or not access_token or not access_token_secret:
	print("missing Twitter API keys, please check setup.py and enter your Twitter API authentication keys into the correct fields")
	exit()

#initiate instance of tweepy using the Twitter account's API keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
			
#the keyword which the script will listen for on Twitter
keyword_to_watch = program_data.keyword_to_watch

#this will be an array of preset messages to follow the @username in the tweet
#but first iterate over the message array and make sure that none of them are too long for a twitter message
tweet_messages = remove_long_messages(program_data.tweet_messages)

#create the camera instance
camera = PiCamera()

# if an images folder hasn't yet been created, then make it now
if not os.path.exists(program_data.filepath):
	os.mkdir(program_data.filepath)

#rotates the camera upside down if necessary
if (program_data.rotate_camera):
	camera.rotation = 180

#start listening for twitter messages
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
myStream.filter(track=[keyword_to_watch], async=True)

print("TweetPiPhoto initiated")
print("Listening for tweets containing \""+program_data.keyword_to_watch+"\"...")
