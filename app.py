from flask import Flask, render_template

app = Flask(__name__)

DEBUG = True
HOST = 'localhost'
PORT = 8000


@app.route('/')
@app.route('/entries')
def index():
    """The homepage / listing view"""
    return render_template('index.html')


@app.route('/entries/new')
def new():
    """The create view"""
    return render_template('new.html')


@app.route('/entries/<id>')
def detail(id):
    """The detail view"""
    return render_template('detail.html', id=id)


@app.route('/entries/<id>/edit')
def edit(id):
    """The edit view"""
    return render_template('edit.html', id=id)


## TODO: Add delete route /entries/<id>/delete


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
