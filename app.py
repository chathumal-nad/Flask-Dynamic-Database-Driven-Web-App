from flask import Flask , render_template

app = Flask(__name__)

ROOMS = [
    {
        'id':1,
        'title': "Deluxe Double",
        'price': 'Rs 35,000',
        'available-rooms': 5
    },
    {
        'id':2,
        'title': "Premium Double",
        'price': 'Rs 45,000',
        'available-rooms': 1 
    },
    {
        'id':3,
        'title': "Presidential Suite",
        'price': 'Rs 95,000',
        'available-rooms': 0 
    },
    {
        'id':4,
        'title': "Sea View Double",
        'price': 'Rs 55,000',
        'available-rooms': 2 
    }        
        ]

@app.route("/home")
def home():
    return render_template('home.html',company="Heritance")


@app.route("/book")
def boot():
    return render_template('book.html',rooms=ROOMS,company="Heritance")

