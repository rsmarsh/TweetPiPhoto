# TweetPiPhoto
when running, this Python script responds to Twitter users who tweet a pre-determined phrase or hashtag. The response is a direct "@" message containing an image which is then captured live from the Raspberry Pi's camera. 

# Installation

First, install python-pip on your Raspberry Pi by entering the following into the terminal:

'sudo apt-get install python-pip'

Then, install the tweepy client on your Pi by entering:

'sudo pip install tweepy'

# Execution

To run the TweetPiPhoto.py script, navigate to the root folder and enter:

'sudo python TweetPiPhoto.py'

To execute and leave the script running in the background after the SSH session has ended, try entering:

'sudo python TweetPiPhoto.py &'

# Set Up

Before the program is operational, some data specific to your Twitter account is required. 
These settings can be altered in the setup.py file.

Other settings which can be changed includes the keyword which the script will be listening and responding to.

You must acquire your Twitter API Keys for the account you wish to tweet from, and enter each individual key in the relevant variables found at the beginning of the setup.py file.

# Configurable Options

Each of the following options can be made, which are found within the setup.py file.
The script must be restarted for any changes to take place.


consumer_key, consumer_secret, access_token, access_token_secret
These are the 4 access variables required for the script to operate. 
This gives the script access to respond to tweets from your account. 
The script does not use your account for any other purposes.


keyword_to_watch
this is the hashtag or phrase the program will listen for
tweets containing this exact keyword will receive the image as a response
replace "#tweetpiphoto" with your desired keyword
e.g. '#LondonWeatherUpdate' or 'New House Building Update' or '@watchingpaintdrylive'

send_message_with_tweet
if you would like an accompanying message to be sent with the tweet, set this to True or False

attach_username_to_end
if you would like the @user tag to appear at the end of the message, then set this to True
this results in your followers being able to see the message in their own timelines

tweet_messages
this is an array of messages which will be sent in the Tweet accompanyting the photo
add as many as you want, they will be randomly selected
empty messages will be ignored

save_image_locally
if you want the pi to save the images it takes locally, as well as posting them to Twitter, then set this to True

image_type
this is a string, e.g. "jpg", and only matters if the above save_image_locally boolean is set to True.
by default, this will save the image as a jpg file, alternatively try using 'png'.

filepath
the directory which each image will be saved locally on the Raspberry Pi, from the root folder
example usage is "images/". 

enable_long_tweets: False
if your account has been enabled to use 280 character tweets, then set this to True
if you do not have 280 character tweets on your account but still set this to True, the script will not work correctly

# Coming Soon

- Automatically follow users who trigger the keyword
- Watch for multiple keywords at once
- broadcast an open tweet not just directed at the original author of the keyword
- access photos already taken from the past in the images folder, e.g. "#keyword, what did the garden look like at 9PM"
- direct images towards another user, e.g. "send @differentuser a picture of my hamster"