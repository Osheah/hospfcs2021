from flask import Flask, render_template, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages', template_folder='templates')


books=[
        {"id":1, "title":"author1",  "price":10},
        {"id":2, "title":"author2",  "price":20},
        {"id":3, "title":"author3",  "price":30}
]
next_id=4
# index
#curl http://127.0.0.1:5000/
@app.route('/')
def index():
  return "Home"

# get all 
#curl -X GET http://127.0.0.1:5000/books
@app.route('/books')
def get_all():
  return jsonify(books)
# find by id
#curl -X GET http://127.0.0.1:5000/books/123

@app.route('/books/<int:id>')
def get_all_by_id(id):
  find_books = list(filter(lambda t: t["id"] ==id, books))
  if len(find_books) ==0:
    return jsonify({}), 204
  return jsonify(find_books)  


  return "served by get_all_id "  + str(id) 



# create
#curl  -i -H "Content-Type:application/json" -X POST -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])  
def create():
  global next_id
  if not request.json:
    abort(400)
  book = {"id":next_id, "title": request.json["title"], "author": request.json["author"], "price":request.json["price"]}
  next_id +=1
  books.append(book)
  return jsonify(book)
# update
# curl -H "Content-Type:application/json" -X PUT -d "{\"title\":\"new title\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])  
def update(id):
  find_books = list(filter(lambda t: t["id"] ==id, books)) 
  if len(find_books) ==0:
    return jsonify({}), 404
  current_book = find_books[0] 
  if 'title' in  request.json:
    current_book['Title']=request.json['title']
  if 'author' in  request.json:
    current_book['author']=request.json['author']   
  if 'price' in  request.json:
    current_book['price']=request.json['price']
  return jsonify(current_book)

# delete
#curl -X DELETE http://127.0.0.1:5000/books/123
@app.route('/books/<int:id>', methods=['DELETE'])  
def delete(id):
  find_books = list(filter(lambda t: t["id"] ==id, books)) 
  if len(find_books) ==0:
    return jsonify({}), 404
  books.remove(find_books[0])   
  return jsonify({"done":True})  


if __name__ =="__main__":
  app.run(debug=True)