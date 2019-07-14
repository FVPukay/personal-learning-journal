from flask import Flask, render_template, redirect, url_for, request
from forms import EntryForm, CatchaForm
from werkzeug.datastructures import MultiDict
from flask_wtf.csrf import CSRFProtect

import models
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

csrf = CSRFProtect(app)

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
    form = EntryForm()
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
    journal_post = models.Entry.select().where(models.Entry.id == id).get()
    return render_template('detail.html', journal_post=journal_post)


@app.route('/entries/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    """The edit view"""
    journal_post = models.Entry.select().where(models.Entry.id == id).get()
    if request.method == 'GET':
        form = EntryForm(
            formdata=MultiDict({
            'title': journal_post.title,
            'date': str(journal_post.date),
            'time_spent': journal_post.time_spent,
            'what_you_learned': journal_post.what_you_learned,
            'resources_to_remember': journal_post.resources_to_remember
            })
        )
    else:
        form = EntryForm()

    if form.validate_on_submit():
        journal_post.title = form.title.data.strip()
        journal_post.date = form.date.data
        journal_post.time_spent = form.time_spent.data
        journal_post.what_you_learned = form.what_you_learned.data.strip()
        # TODO: Refactor the line below so it's <= 79 characters
        journal_post.resources_to_remember = form.resources_to_remember.data.strip()
        journal_post.save()
        return redirect(url_for('index'))
    return render_template('edit.html', form=form, journal_post=journal_post)


## TODO: Add delete route /entries/<id>/delete
@app.route('/entries/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    """The delete view"""
    journal_post = models.Entry.select().where(models.Entry.id == id).get()
    form = CatchaForm()
    catcha_code = 'Meow!'
    if form.validate_on_submit() and form.catcha_code.data == catcha_code:
        journal_post.delete_instance()
        return redirect(url_for('index'))
    return render_template('delete.html', form=form, journal_post=journal_post, catcha_code=catcha_code)


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
