#    Twitter Settings. Not kept with the main django settings file.
#    To access these settings use:
#    
#    from ut_twitter import setings
#
#    in your view

REQUEST_TOKEN_URI = 'https://api.twitter.com/oauth/request_token'
AUTH_TOKEN_URI = 'https://api.twitter.com/oauth/authorize'
ACCESS_TOKEN_URI = 'https://api.twitter.com/oauth/access_token'
DISPLAY_NAME = ''
USER_ID = ''
#    The ACCESS_TOKEN* settings only work for accessing your own twitter account, they must be generated when you create your account.
#    3rd party apps will still require your authorisation, so follow the Twython docs for dealing with that
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

AUTH_TOKEN = ACCESS_TOKEN

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

COUNT_LIMIT = 1