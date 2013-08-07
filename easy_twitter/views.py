from twython import Twython

from easy_twitter.models import Settings

def get_tweets(account):
    feed_account = Settings.objects.get(display_name=account)
    twitter = Twython(feed_account.consumer_key, feed_account.consumer_secret, feed_account.access_token, feed_account.access_token_secret)
    time_line = twitter.get_user_timeline(display_name=feed_account.display_name, include_rts=feed_account.show_retweets, count=feed_account.count_limit, exclude_replies=feed_account.exclude_replies)
    return time_line

def show_tweets(account):
    tweets = get_tweets(account)
    return tweets
    


