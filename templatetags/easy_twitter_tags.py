import datetime
from django import template

register = template.Library()

from easy_twitter.views import show_tweets
from easy_twitter.settings import DISPLAY_NAME

@register.inclusion_tag('easy_twitter/twitter.html', takes_context=True)
def show_tweet(context):
    return {
            'tweets' : show_tweets(),
            'user' : DISPLAY_NAME
            }

@register.filter(is_safe=True)
#    This takes the text in the tweet and uses the API's urls indices to parse each url and replace the plain text with the actual url link
#    Please ensure you use |safe in the template after this tag
def parse_urls(text, urls):
    for url in urls:
        text = text.replace(text[url['indices'][0]:url['indices'][1]], "<a href='%s'>%s</a>" % (url['expanded_url'], url['display_url']))
    return text
    

@register.filter(is_safe=True)
#    For the with time option you must supply True if you want to add the H:M time option
def nice_date(date, with_time=False):
    date = date.split(' ')
    #    strptime does not support %z (python 2.7), so I have to split and restring the date to strptime likes it
    py_date = datetime.datetime.strptime("%s %s %s %s %s" % (date[0], date[1], date[2], date[3], date[5]), '%a %b %d %H:%M:%S %Y')
    if with_time:
        nice_date = py_date.strftime("%a %d %b %Y at %H:%M")
    else:
        nice_date = py_date.strftime("%a %d %b %Y")
    return nice_date
    