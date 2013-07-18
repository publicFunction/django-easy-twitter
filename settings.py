#    Twitter Settings. Not kept with the main django settings file.
#    To access these settings use:
#    
#    from ut_twitter import setings
#
#    in your view

REQUEST_TOKEN_URI = 'https://api.twitter.com/oauth/request_token'
AUTH_TOKEN_URI = 'https://api.twitter.com/oauth/authorize'
ACCESS_TOKEN_URI = 'https://api.twitter.com/oauth/access_token'
DISPLAY_NAME = 'pasmaltd'
USER_ID = '83575214'
#    The ACCESS_TOKEN* settings only work for accessing your own twitter account, they must be generated when you create your account.
#    3rd party apps will still require your authorisation, so follow the Twython docs for dealing with that
ACCESS_TOKEN = '83575214-LSNynwFCYpDeFoTDNsNVK0PjSKPkd9o1EyYPiHwM'
ACCESS_TOKEN_SECRET = 'ZD5GIASCixOuwbnViNbwjZfXQ7g543491XB63Jk8c'

AUTH_TOKEN = ACCESS_TOKEN

CONSUMER_KEY = 'oCGp56ixrt7CJMTIqr8sdw'
CONSUMER_SECRET = '95QZ4VRv4aiENGVwfpHq9N6bsloqTatKIFclYZGacE'

COUNT_LIMIT = 1