import time
import random
from instagrapi import Client

# Instagram Bot Configuration
USERNAME = "amagicmomentshop"
PASSWORD = "11490203Tone!"

cl = Client()
cl.login(USERNAME, PASSWORD)

def smart_delay():
    time.sleep(random.uniform(30, 90))  # Randomized delay to mimic human behavior

def like_and_follow_by_hashtag(hashtags, max_actions=20):
    actions = 0
    for tag in hashtags:
        posts = cl.hashtag_medias_recent(tag, 10)
        for post in posts:
            if actions >= max_actions:
                return
            try:
                cl.media_like(post.id)
                cl.user_follow(post.user.pk)
                actions += 1
                smart_delay()
            except Exception as e:
                print(f"Error: {e}")

def comment_on_posts(hashtags, comments, max_comments=10):
    actions = 0
    for tag in hashtags:
        posts = cl.hashtag_medias_recent(tag, 10)
        for post in posts:
            if actions >= max_comments:
                return
            try:
                comment = random.choice(comments)
                cl.media_comment(post.id, comment)
                actions += 1
                smart_delay()
            except Exception as e:
                print(f"Error: {e}")

def unfollow_non_followers():
    followers = cl.user_followers(cl.user_id)
    following = cl.user_following(cl.user_id)
    for user in following:
        if user not in followers:
            try:
                cl.user_unfollow(user)
                smart_delay()
            except Exception as e:
                print(f"Error: {e}")

# Define engagement parameters
hashtags = ["disneyworld", "disneyland", "universalstudios", "themepark", "disneylandcalifornia", "universalhollywood", "losangeleslife", "hollywoodstudios", "disneygram", "magickingdom", "disneylife", "disneyparks"]
comments = ["Love this! 😍", "Such a magical moment! ✨", "Theme park vibes are the best! 🎢"]

# Run bot actions
if __name__ == "__main__":
    like_and_follow_by_hashtag(hashtags)
    comment_on_posts(hashtags, comments)

# To be scheduled: Unfollow non-followers after one year
