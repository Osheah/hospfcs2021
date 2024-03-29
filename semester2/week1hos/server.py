from flask import Flask, render_template, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

#@app.route('/')
#def index():
#  return render_template('index.html')

@app.route('/')
def index():
  return redirect(url_for('login'))

@app.route('/login')
def login():
  abort(401)
  return "served by login"

@app.route('/user')
def get_user():
  return "Served by get_user"
@app.route('/user/<int:id>')
def get_user_by_id(id):
  return "Served by get_user_by_id = " + str(id)

@app.route('/user', methods=['POST'])
def create_user():
  return "Served by create_user"

@app.route('/demo_url_for')
def demo_url_for():
  returnString = "url for index is "+url_for('index')
  returnString += "<br />"
  returnString += "url for get_user_by_id " + url_for('get_user_by_id', id=12) 
  return returnString

@app.route('/demo_request', methods=['POST', 'GET', 'DELETE'])
def demo_request():
  return request.method


  

if __name__ =="__main__":
  app.run(debug=True)