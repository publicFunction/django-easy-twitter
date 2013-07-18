django-easy-twitter
===================

Easy Twitter Feed for Django

This allows you to put a basic twitter feed for your own account onto a page template.

This app makes use of Twython so please install that first before using, or add it to your own requirements.txt file:
  
  pip install twython
  
Once installed just add it to your installed apps:

	INSTALLED_APPS = (
						...
						'easy_twitter',
						...
					)

Add templates can be picked up and add:

  os.path.join(PROJECT_PATH, "easy_twitter", "templates"),

to your own TEMPLATE_DIRS = ( ... ) tuple

Run Sync DB.
Then run manage.py migrate --fake (if you use south)

Once all done you can then head to https://dev.twitter.com/apps and create a new application, if you have not already, 
and create it. Following these steps (you must have a valid twitter account to login):

	Name
	Description
	Website
	Callback URL (make this the same as your website setting, this plugin wont really make use of it)
	Agree to the Terms and fill in the captcha

You will then get redirected to your new twitter app.

Copy your Consumer Key and Secret into the settings.
Change the URI's if they differ from the default ones
Then click the Create My Access Token Button and copy these settings into the model.

Once done ... TBC


OAuth is only required when creating an app that access other peoples twittter accounts this app is not designed for that, it is 
a simple way to pull your own feed onto your site.
