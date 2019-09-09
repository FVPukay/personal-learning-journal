# Personal Learning Journal

#### What this web app does
This app allows users to post, edit, and delete journal entries.  When
creating or editing a journal entry, a user will enter a title, time spent,
what they learned, and resources to remember. There is a listing page where
users will see all the posted journal entries and pages to edit and delete
journal entries.

`Languages Used:` Python 3, HTML, CSS, Jinja2  
`Framework:` Flask  
`Database:` Sqlite3  
`ORM:` Peewee
`Hosted:` Heroku

##### Screenshots of the UI
[Personal Learning Journal](https://www.flickr.com/photos/156561177@N03/albums/72157709664341772)

##### How to run work_log.py
Creating a Virtualenv is highly recommended.

Please refer to the requirements.txt file to see a list of the dependencies
(matching the versions is the safest way to be sure the app works as expected)
but the following pip installs can be done for quick setup:

>`pip install Flask-WTF`  
`pip install peewee`

`Note:` `pip install Flask-WTF` should install Flask so `pip install Flask`
should not be needed unless specific versions of Flask, peewee, etc are
installed.

The app can be run by using:
>`python app.py`
