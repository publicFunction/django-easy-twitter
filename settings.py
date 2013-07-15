#    Twitter Settings. Not kept with the main django settings file.
#    To access these settings use:
#    
#    from ut_twitter import setings
#
#    in your view

REQUEST_TOKEN_URI = 'https://api.twitter.com/oauth/request_token'
AUTH_TOKEN_URI = 'https://api.twitter.com/oauth/authorize'
ACCESS_TOKEN_URI = 'https://api.twitter.com/oauth/access_token'
DISPLAY_NAME = 'public_Function'
USER_ID = '121380883'
#    The ACCESS_TOKEN* settings only work for accessing your own twitter account, they must be generated when you create your account.
#    3rd party apps will still require your authorisation, so follow the Twython docs for dealing with that
ACCESS_TOKEN = '121380883-fwIEUzrlBcg1ALjpih5BPcnYjkwleeSt5hC9p3wp'
ACCESS_TOKEN_SECRET = 'Zcnx1L5KuIUyG5CUMoiob3v7QsD9aSO5BP2WHqM4'

AUTH_TOKEN = ACCESS_TOKEN

CONSUMER_KEY = 'zQ6QgNBbdA6eFD5M6ZbLjw'
CONSUMER_SECRET = 'Zf8OrR3ITe1P7accVrgfontiuIbb846yGLaMKZZKdLc'

COUNT_LIMIT = 1