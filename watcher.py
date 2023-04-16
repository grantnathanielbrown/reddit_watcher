import praw
import time
import simpleaudio as sa
import os
import argparse
from dotenv import load_dotenv

load_dotenv()

# Use the secret_key in your script
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
user_agent = "reddit_watcher by /u/username"

# Authenticate with the Reddit API
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

sound_file = "./AUGH.wav"

def play_sound():
    wave_obj = sa.WaveObject.from_wave_file(sound_file)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def process_submission(submission):
    print(f"New post: {submission.title} (https://www.reddit.com{submission.permalink}) by {submission.author}")
    play_sound()

def poll_subreddit(subreddit_name, polling_interval):
    last_polled = None

    while True:
        print(f"Polling r/{subreddit_name}...")

        submissions = reddit.subreddit(subreddit_name).new(limit=10)
        
        if last_polled:
            new_submissions = [s for s in submissions if s.created_utc > last_polled]

            for submission in new_submissions:
                process_submission(submission)

        last_polled = time.time()
        time.sleep(polling_interval)

def main():
    parser = argparse.ArgumentParser(description='Poll a subreddit for new posts.')
    parser.add_argument('-s', '--subreddit', default='collectibleavatars', help='Subreddit name to poll (default: collectibleavatars)')
    parser.add_argument('-i', '--interval', type=int, default=60, help='Polling interval in seconds (default: 30)')

    args = parser.parse_args()

    poll_subreddit(args.subreddit, args.interval)

if __name__ == "__main__":
    main()
