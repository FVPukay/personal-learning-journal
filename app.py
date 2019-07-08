from flask import Flask, render_template, redirect, url_for

import forms
import models
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

DEBUG = True
HOST = 'localhost'
PORT = 8000


@app.route('/')
@app.route('/entries')
def index():
    """The homepage / listing view"""
    journal_posts = models.Entry.select().limit(100)
    return render_template('index.html', journal_posts=journal_posts)


@app.route('/entries/new', methods=['GET', 'POST'])
def new():
    form = forms.AddEntryForm()
    if form.validate_on_submit():
        models.Entry.create(
            title=form.title.data.strip(),
            date=form.date.data,
            time_spent=form.time_spent.data,
            what_you_learned=form.what_you_learned.data.strip(),
            resources_to_remember=form.resources_to_remember.data.strip()
        )
        return redirect(url_for('index'))
    return render_template('new.html', form=form)


@app.route('/entries/<int:id>')
def detail(id):
    """The detail view"""
    journal_post = models.Entry.select().where(models.Entry.id == id)
    return render_template('detail.html', journal_post=journal_post)


@app.route('/entries/<id>/edit')
def edit(id):
    """The edit view"""
    return render_template('edit.html', id=id)


## TODO: Add delete route /entries/<id>/delete


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
