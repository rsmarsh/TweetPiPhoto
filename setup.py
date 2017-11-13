#enter the authentication information provided by Twitter in this file
#Twitter Authenticat
#twitter authentication variables:
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

#Camera Rotation
#if your images are upside down, then set the below to True
rotate_camera = True


#Tweet Settings:
#this is the hashtag or phrase the program will listen for
#tweets containing this exact keyword will receive the image as a response
#replace "#tweetpiphoto" with your desired keyword
#e.g. '#LondonWeatherUpdate' or 'New House Building Update' or '@watchingpaintdrylive'
keyword_to_watch = "#tweetpiphoto"

#if you would like an accompanying message to be sent, set this to true or false:
send_message_with_tweet = True,

#if you would like the @user tag to appear at the end of the message, then set this to True
#this results in your followers being able to see the message in their own timelines
attach_username_to_end = False

#messages which will be sent in the Tweet accompanyting the photo
#add as many as you want, they will be randomly selected
#empty messages will be ignored
tweet_messages = [
	"Here is your photo!",
	"How are we looking?",
	"",
]

#Photo Settings:
#if you want the pi to save the images it takes locally, as well as posting them to Twitter, then set this to True
save_image_locally = True

#the followingn settings only matter if the above save_image_locally boolean is set to true;
#by default, this will save the image as a .jpg, alternatively try 'png', this only affects 
image_type = "jpg"

# the directory which each image will be saved locally on the Raspberry Pi the /images folder
#this folder will be automatically created when the program is first run
#this is required even if you are not saving the images locally, as they must be temporarily stored
filepath = "images/"

#Twitter has recently allowed 280 character tweets, leave this as True to support these
#if you do not have 280 character tweets on your account but still set this to True, the script will not work correctly
enable_long_tweets = True