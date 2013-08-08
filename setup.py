from distutils.core import setup

setup(
    name='django-easy-twitter',
    version='0.1.0',
    author='Chris Moss',
    description='Simple way to get your chosen twitter feed onto your project',
    long_description=open('README.md').read(),
    author_email='chris@publicfunction.co.uk',
    keywords='django twitter easy twitter easy-twitter',
    install_requires=['django', 'twython'],
    url='https://github.com/publicFunction/django-easy-twitter',
    packages=[
        'easy_twitter',
        'easy_twitter.templatetags',
    ],
    package_data={
        'easy_twitter': [
            'easy_twitter/templates/easy_twitter/*',
        ],
    },
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)