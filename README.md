# Personal Learning Journal
* Users can to post, edit, and delete journal entries
* This is a [Flask](https://flask.palletsprojects.com/en/2.2.x/) app
* The ORM is [Peewee](http://docs.peewee-orm.com/en/latest/#)

## Backend
* See [app.py](https://github.com/FVPukay/personal-learning-journal/blob/master/app.py) to view the routes, setup, and error handling
* See [models.py](https://github.com/FVPukay/personal-learning-journal/blob/master/models.py) for database setup
* See [forms.py](https://github.com/FVPukay/personal-learning-journal/blob/master/forms.py)

## Frontend
* See [templates](https://github.com/FVPukay/personal-learning-journal/tree/master/templates) with Jinja2 template logic
    * See [404.html](https://github.com/FVPukay/personal-learning-journal/blob/master/templates/404.html)
    * See [base.html](https://github.com/FVPukay/personal-learning-journal/blob/master/templates/base.html)
    * See [csrf_error.html](https://github.com/FVPukay/personal-learning-journal/blob/master/templates/csrf_error.html)
    * See [delete.html](https://github.com/FVPukay/personal-learning-journal/blob/master/templates/delete.html)
    * See [detail.html](https://github.com/FVPukay/personal-learning-journal/blob/master/templates/detail.html)
    * See [edit.html](https://github.com/FVPukay/personal-learning-journal/blob/master/templates/edit.html)
    * See [index.html](https://github.com/FVPukay/personal-learning-journal/blob/master/templates/index.html)
    * See [macros.html](https://github.com/FVPukay/personal-learning-journal/blob/master/templates/macros.html)
        * See [edit.html](https://github.com/FVPukay/personal-learning-journal/blob/master/templates/edit.html) and [new.html](https://github.com/FVPukay/personal-learning-journal/blob/master/templates/new.html) to see how macros are used
    * See [new.html](https://github.com/FVPukay/personal-learning-journal/blob/master/templates/new.html)

## Screenshots of Personal Learning Journal
* See [these photos](https://www.flickr.com/photos/156561177@N03/albums/72157709664341772)

## How to run work_log.py
Creating a [Virtualenv](https://pythonbasics.org/virtualenv/) is highly recommended

See [requirements.txt](https://github.com/FVPukay/personal-learning-journal/blob/master/requirements.txt) to view dependencies
* matching the versions is the safest way to be sure the app works as expected but the following pip installs can be done for quick setup

>`pip install Flask-WTF`  
`pip install peewee`

`Note:` `pip install Flask-WTF` should install Flask so `pip install Flask`
should not be needed unless specific versions of Flask, Peewee, etc. are
installed

The app can be run by using:
>`python app.py`
