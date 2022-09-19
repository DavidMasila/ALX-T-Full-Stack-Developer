from flask import jsonify, request, abort
from app import app, Book, db



@app.after_request
def after_request(request):
    request.headers.add(
        "Allow-Control-Access-Headers","Content-Type, Authorization, true"
    )
    request.headers.add(
        "Allow-Control-Access-Mthods","GET,PUT,PATCH,POST,DELETE,OPTIONS"
    )

    return request

start_page = 8

@app.route('/books', methods=['GET','POST'])
def all_books():
    #implement pagination
    pages = request.args.get('page',1,type=int)#get page no. otherwise default to 1
    start = (pages - 1) * start_page
    end = start + start_page
    all_books = Book.query.order_by(Book.id).all()
    books=[book.format() for book in all_books]
    current_books=books[start:end]

    if len(current_books) == 0:
        abort(404)
    else: 
        return jsonify({
            "success":True,
            "books": current_books,
            "total_book": len(all_books)
     })

@app.route('/books/<int:book_id>',methods=['GET','POST'])
def get_specific_book(book_id):
    specific_book=Book.query.filter(Book.id == book_id).one_or_none()

    if specific_book is None:
        return abort(404)
    else:
        return jsonify({
            "success":True,
            "Specific_book": specific_book.format()
        })

@app.route('/books/<int:book_id>',methods=['PATCH'])
def update_book(book_id):
    body = request.get_json()

    try:
        book = Book.query.filter(Book.id == book_id).one_or_none()

        if book is None:
            abort(404)
        else:
            if 'rating' in body:
                book.rating = int(body.get('rating'))

            book.update()

            return jsonify({
                "success":True,
                "id":book.id
            })

    except:
        abort(400)


@app.route('/books/delete/<int:book_id>', methods=['DELETE'])
def delete_specific_book(book_id):
    try:
        delete_this_book = Book.query.get(book_id)
        delete_this_book.delete()

        return jsonify({
            "success":True,
            "deleted book id":book_id,
            "Number of books":len(Book.query.all())
        })
        
    except:
        abort(400)

@app.route('/books/new-book',methods=['POST'])
def add_new_book():

    body = request.get_json()

    new_title = body.get('title')
    new_author = body.get('author',None)
    new_rating = body.get('rating',None)

    try:
        book = Book(title=new_title, author=new_author, rating=new_rating)
        book.insert()

        all_books = Book.query.order_by(Book.id).all()
        books_all = [book.format() for book in all_books]
        return jsonify({
            "success": True,
            "All books": books_all
        })
    except:
        abort(422)

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success":False,
        "error":404,
        "message":"resource not found"
    }),404

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success":False,
        "error":422,
        "message":"Unprocessable"
    }),422

@app.errorhandler(400)
def unprocessable(error):
    return jsonify({
        "success":False,
        "error":400,
        "message":"Bad Request"
    }),400