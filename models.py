'''
    This Model replaces the old settings.py file
'''
from django.db import models
from django.core.exceptions import ValidationError


def restrict_to_only_one(object):
    model = object.__class__
    if (model.objects.count() > 0 and object.id != model.objects.get().id):
        raise ValidationError("You can only have one set of settings for these %s" % model.__name__)

#    The ACCESS_TOKEN* settings only work for accessing your own twitter account, they must be generated when you create your account app.
#    3rd party apps will still require your authorisation, so follow the Twython docs for dealing with that. This app is only designed
#    to allow you to place your own twitter feeds onto a site.
class Settings(models.Model):
    request_token_uri = models.URLField(max_length=500, default="https://api.twitter.com/oauth/request_token")
    auth_token_uri = models.URLField(max_length=500, default="https://api.twitter.com/oauth/authorize")
    access_token_uri = models.URLField(max_length=500, default='https://api.twitter.com/oauth/access_token')
    display_name = models.CharField(max_length=200, help_text='This is your Twitter Account name without the @.')#'pasmaltd'
    user_id = models.IntegerField(blank=True, null=True, help_text='This is optional, as toy may have to get your ID from a 3rd Party source.')#USER_ID = '83575214'
    access_token = models.CharField(max_length=100)#'83575214-LSNynwFCYpDeFoTDNsNVK0PjSKPkd9o1EyYPiHwM'
    access_token_secret = models.CharField(max_length=100)#'ZD5GIASCixOuwbnViNbwjZfXQ7g543491XB63Jk8c'
    auth_token = models.CharField(max_length=100, blank=True, null=True)
    consumer_key = models.CharField(max_length=100)#'oCGp56ixrt7CJMTIqr8sdw'
    consumer_secret = models.CharField(max_length=100)#95QZ4VRv4aiENGVwfpHq9N6bsloqTatKIFclYZGacE'
    count_limit = models.IntegerField(help_text='This is the number of tweets you want to appear')#COUNT_LIMIT = 1
    
    def __unicode__(self):
        return self.display_name
    
    def clean(self):
        restrict_to_only_one(self)