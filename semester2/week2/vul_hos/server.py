from flask import Flask,session, url_for, request, redirect, abort, jsonify, render_template
app = Flask(__name__, static_url_path='', static_folder='staticpages')
from  dao import dao

# just using POST for simplicity

# design the home page
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def create():
    forms = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "comment": request.form['comment'],
    }
    return jsonify(dao.create(forms))





@app.route('/sqlinjection')
def sqlinjection():
  return render_template('sqlinjection.html')

@app.route('/sqlinjection', methods=['POST'])
def bad_create():
    forms = {
        "email": request.form['email']
    }
    return jsonify(dao.bad_create(forms['email']))


if __name__ == "__main__":
    app.run(debug=True)