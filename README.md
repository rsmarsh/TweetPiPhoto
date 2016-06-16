# TweetPiPhoto
@replies to each user who tweets a pre-determined phrase or hashtag with an image taken from the Raspberry Pi's camera. 

Installation

First, install python-pip on your Raspberry Pi by entering the following into the terminal:

sudo apt-get install python-pip

Then, install the tweepy client on your Pi by entering:

sudo pip install tweepy

Now execute the TweetPiPhoto.py script from the TweetPiPhoto Repository by navigating to the root folder and entering:

sudo python TweetPiPhoto.py

To execute and leave the script running in the background after the SSH session has ended, try entering:

sudo python TweetPiPhoto.py &

Set Up

Some settings must be changed before it will be operational.

Acquire your Twitter API Keys for the account you wish to tweet from into each individual variable at the beginning of the TweetPiPhoto.py file.
Edit the variable named message_with_photo. This will be the message which is sent along with the image
Edit the variable named keyword_to_watch. This is the keyword that the program will watch for on twitter
This is an early version and more features will be added later
