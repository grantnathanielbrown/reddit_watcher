# reddit_watcher 

reddit_watcher is a Python script that monitors subreddits and plays an audio file (default is the voice of [Mr. Ride](https://www.youtube.com/shorts/fTCKVLNDs20)
) whenever someone makes a new post.

I made this when I was waiting on the Reddit avatar NFTs to be released and didn't want to just sit on the subreddit refreshing the page over and over again. Should be useful for similar circumstances, like if you're waiting for some kind of announcement.

## SET UP WITH REDDIT

To use the Reddit API for polling a subreddit, you'll need to register your application and get the necessary credentials (client ID and client secret). Here's a step-by-step guide to doing so

Register your application on Reddit:

Go to https://www.reddit.com/prefs/apps
Click "Create App" or "Create Another App"
Fill in the required fields (name, description, etc.)
Choose "script" as the application type
Set the redirect URI to "http://localhost:8080"
Click "Create app" and note the client ID and client secret

## INSTALL PACKAGES 

install python
pip install praw
pip install simpleaudio
pip install python-dotenv

## EXPORT CLIENT ID AND SECRET

create .env file
add the following text to the file:
CLIENT_ID=(your client id here)
CLIENT_SECRET=(your client secret here)

## RUN SCRIPT / OPTIONS

Here's an example of how to run the script
python watcher.py -s askreddit -i 30

this would run the script watching the AskReddit subreddit, polling it every 30 seconds. 

If you just run python watcher.py you get the defaults (CollectibleAvatars, 60 seconds)

## OTHER / FAQ

### The reddit API has a rate limit of 60 requests per minute. Since you're trying to detect every single new post ASAP, why not poll as often as possible?

It seems that the lower you set the interval, the more likely it is that the script will miss posts. 30 - 60s seems to be a good range that gives you a balance between detecting posts as quickly as possible and not missing any.

If I have time in the future I will debug it.

### Why do I have to make my own application? Why can't I just use yours?

Reddit API rate limit. Every single time the script polls a subreddit, you're making a request to the API.