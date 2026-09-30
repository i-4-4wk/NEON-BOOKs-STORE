from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import sqlite3
from dbconfig import book, database, app, client
import os


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'} #https://flask.palletsprojects.com/en/stable/patterns/fileuploads/
os.makedirs('static/uploads', exist_ok=True)
cart_items = []

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def base():
    books = book.query.all()
    return render_template('client.html', books = books)

@app.route('/addbook', methods = ['GET','POST'])
def add_book():
   if (request.method == 'POST'):
       title = request.form.get('title')
       readme = request.form.get('readme')
       author = request.form.get('author')
       price = float(request.form.get('price'))
       category = request.form.get('category')
       book_cover = None
       if('cover' in request.files):
          file = request.files['cover']
          if(file.filename != ''):
              if(file and allowed_file(file.filename)):
                  filename = secure_filename(file.filename)
                  book_cover = filename
                  file.save(os.path.join('static/uploads', book_cover))
             


               

       print("=============================================\n")
       print(f"title: {title}")
       print(f"readme: {readme}")
       print(f"author: {author}")
       print(f"price: {price}")
       print(f"category: {category}")
       if(book_cover):
           print("the book cover is imported, state: good")
       else:
           print("the book cover import failled, state: bad !!!")
       print("=============================================\n")

       new_book = book(title = title,readme = readme, author = author, price =price, cover = book_cover, category=category)
       database.session.add(new_book)
       database.session.commit()
       return redirect(url_for('admin'))
   return render_template('add_book.html')

@app.route('/admin', methods = ['GET', 'POST'])
def admin():

    if (request.method == 'POST'):
        book_id = request.form.get('delete_id')
        book_item = book.query.get(book_id)

        if book_item.cover:
           cover_path = os.path.join('static/uploads', book_item.cover)
           if os.path.exists(cover_path):
            os.remove(cover_path)

        database.session.delete(book_item)
        database.session.commit()
 
    books = book.query.all()
    return render_template('admin.html', books = books)

@app.route('/buybook/<int:bookid>', methods = ['GET', 'POST'])
def buy(bookid):
    book_i = book.query.get(bookid)
    global cart_items

    if (request.method == 'POST'):
        quantity = int(request.form.get('quantity', 1))
        title = book_i.title
        price = book_i.price

        cart_items.append([title, quantity, price])
        
        print("===============================================================")
        print(f"Added: {title} x {quantity}")
        print(f"Cart: {cart_items}")
        print("===============================================================")
        
        return redirect(url_for('base'))
    
    return render_template('buybook.html', book=book_i)

@app.route('/cart', methods = ["GET","POST"])
def cart():
    global cart_items
    print("===============================================================")
    print(f"cart.page cart: {cart_items}")
    print("===============================================================")
    total =  0
    

    for i in range(len(cart_items)):
        total += cart_items[i][2] * cart_items[i][1]

    print("===============================================================")
    print(f"the Total is: {total} DA, state: Calculated")
    print("===============================================================")

    if(request.method == 'POST'):
        name = request.form.get('clientname')
        number = request.form.get('clientnumber')
        addr = request.form.get('shippingaddr')
        for j in cart_items:
            title = j[0]
            quantity = j[1]
            new_client = client(name = name, number = number, addr = addr, title = title, quantity = quantity)
            database.session.add(new_client)

        database.session.commit()
        if True: 
         print('state: good !!!')
         cart_items=[]
         total = 0

    return render_template('cart.html', total=total, cart_items = cart_items)
    
@app.route('/admin/panel', methods=['GET','POST'])
def panel():
    if(request.method == 'POST'):
        order_id = request.form.get('done')
        order = client.query.get(order_id)
        if order:
            database.session.delete(order)
            database.session.commit()
        return redirect(url_for('panel'))


    orders = client.query.all()

    print("===============================================================")
    for order in orders:
        print(f"  #{order.id} | {order.name} | {order.title} | {order.quantity}")
    print("===============================================================")


    return render_template('adminpanel.html', orders = orders)

if(__name__ == '__main__'):
    app.run(debug = True)


