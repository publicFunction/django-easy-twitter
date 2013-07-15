from twython import Twython
from ut_twitter import settings as tw_settings

def get_tweets():
    twitter = Twython(tw_settings.CONSUMER_KEY, tw_settings.CONSUMER_SECRET, tw_settings.ACCESS_TOKEN, tw_settings.ACCESS_TOKEN_SECRET)
    time_line = twitter.get_user_timeline(display_name=tw_settings.DISPLAY_NAME, include_rts=False, count=tw_settings.COUNT_LIMIT)
    return time_line

def show_tweets():
    tweets = get_tweets()
    return tweets
    


