django-easy-twitter
===================

Easy Twitter Feed for Django

This allows you to put a basic twitter feed for you own account onto a page template.

This app makes use of Twython so please install that first before using, or add it to your own requirements.txt file:
  
  pip install twython

Just replace the settings from your own Twitter app details and make sure to generate you API Data. OAuth is only 
required when creating an app that access other peoples twittter accounts this app is not designed for that, it is 
a simple way to pull your own feed onto your site.
